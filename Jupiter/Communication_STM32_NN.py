import serial
import numpy as np

PORT = "COM5"

def synchronise_UART(serial_port):
    while True:
        serial_port.write(b"\xAB")
        ret = serial_port.read(1)
        if ret == b"\xCD":
            serial_port.read(1)
            break

def send_inputs_to_STM32(inputs, serial_port):
    inputs = inputs.astype(np.float32)
    buffer = b"".join(x.tobytes() for x in inputs)
    serial_port.write(buffer)

def read_output_from_STM32(serial_port):
    output = serial_port.read(5)
    return [int(out) / 255 for out in output]

def evaluate_model_on_STM32(iterations, serial_port):
    accuracy = 0
    label_counts = np.zeros(Y_test.shape[1])  # Pour compter le nombre de chaque label
    correct_counts = np.zeros(Y_test.shape[1])  # Pour compter les prédictions correctes par label

    with open("evaluation_results.txt", "w") as file:  # Ouverture du fichier
        for i in range(iterations):
            log = f"----- Iteration {i+1} -----\n"
            send_inputs_to_STM32(X_test[i], serial_port)
            output = read_output_from_STM32(serial_port)
            
            expected_label = np.argmax(Y_test[i])
            predicted_label = np.argmax(output)
            
            label_counts[expected_label] += 1
            if predicted_label == expected_label:
                accuracy += 1 / iterations
                correct_counts[expected_label] += 1
            
            log += f"   Expected output: {Y_test[i]}\n"
            log += f"   Received output: {output}\n"
            log += f"----------------------- Accuracy: {accuracy:.2f}\n\n"
            print(log)
            file.write(log)
        
        # Calcul de l'accuracy moyenne par label
        label_accuracy = correct_counts / label_counts
        
        # Conclusion
        conclusion = "\n----- Conclusion -----\n"
        conclusion += f"Global Accuracy: {accuracy:.2f}\n"
        conclusion += "Accuracy per label:\n"
        for label, acc in enumerate(label_accuracy):
            conclusion += f"   Label {label}: {acc:.2f} (Count: {int(label_counts[label])})\n"
        conclusion += "-----------------------\n"
        
        print(conclusion)
        file.write(conclusion)  # Écriture de la conclusion dans le fichier
    
    return accuracy

if __name__ == '__main__':
    X_test = np.load("./Jupiter/Xtest.npy")
    Y_test = np.load("./Jupiter/Ytest.npy")

    with serial.Serial(PORT, 115200, timeout=1) as ser:
        print("Synchronising...")
        synchronise_UART(ser)
        print("Synchronised")

        print("Evaluating model on STM32...")
        error = evaluate_model_on_STM32(100, ser)