Ceci est le fruit du travail de Jade MELLITI et Alexandra BARON. 

# Rapport de Projet - Maintenance Prédictive sur STM32L4R9

## Table des Matières
1. [Introduction](#introduction)
2. [Objectifs](#objectifs)
3. [Architecture du Projet](#architecture-du-projet)
4. [Développement du Modèle ML](#-développement-du-modèle-ml)
5. [Intégration sur STM32](#-intégration-sur-stm32)
6. [Analyse des Performances](#-analyse-des-performances)
7. [Prise de Recul](#-prise-de-recul)
8. [Conclusion](#-conclusion)

## Introduction
Ce projet vise à concevoir, entraîner et déployer un réseau de neurones profond (DNN) en Python pour la maintenance prédictive, en utilisant le jeu de données **AI4I 2020 Predictive Maintenance Dataset**. L'objectif final est d'exporter le modèle pour une exécution sur une carte **STM32L4R9**.

## Objectifs
1. **Prétraitement des données** : Nettoyage et équilibrage du dataset.
2. **Conception et entraînement du modèle** : Architecture DNN optimisée.
3. **Évaluation des performances** : Métriques de classification et matrice de confusion.
4. **Conversion pour cible embarquée** : Export au format TFLite.
5. **Intégration sur STM32** : Déploiement via STM32CubeIDE.

## Architecture du Projet

IA_EMBARQUE/
├── 📂 Firmware/
│   ├── 📂 App/                # Configuration X-Cube-AI
│   │   ├── app_x-cube-ai.c    # Interface AI
│   │   └── ...                # Fichiers générés
│   │
│   └── 📂 Core_Src/           # Logique applicative
│       └── main.c             # Point d'entrée
│
├── 📂 images/                 # Graphiques
│   ├── training_accuracy.png
│   └── confusion_matrix.png
│
└── 📂 Jupiter/                # Développement IA
    ├── 📄 TP_IA_EMBARQUEE.ipynb  # Entraînement
    └── 📄 *.tflite            # Modèle optimisé

IA_EMBARQUE/

├── Firmware/                               # Programmes réalisés sur STM32CubeIDE

│   ├── App

|   |     └── app_x-cube-ai.c
|   |     └── ia_embarque_data_params.c
|   |     └── ia_embarque_data.c
|   |     └── ia_embarque_generate_report.txt
│   └── Core_Src
|   |     └── main.c
├── images/                                 # Résultats du JupiterNoteBook.
├── Jupiter/                                # Notebooks d'analyse et codes pythons de communications + les résultats
│   └── TP_IA_EMBARQUEE.ipynb               # Notebook
│   └── ai4i2020.csv                        # Dataset
│   └── Communication_STM32_NN.py           # Code python pour l'inférence / Communication par Uart avec STM32 
│   └── my_mlp_model.h5                     # Modèle au format h5
│   └── my_mlp_model.tflite                 # Modèle au format tflite
│   └── Xtest.npy                           # Données de test
│   └── Ytest.npy                           # Données de test
└── evaluation_results.txt                  # Résultats + CONCLUSION 
└── README.md


IA_EMBARQUE/
├── Firmware/ # Code STM32CubeIDE (inférence, gestion des données)
│ ├── App/ # Fichiers générés par X-Cube-AI
│ └── Core_Src/ # Code principal (main.c)
├── images/ # Visualisations des résultats (matrices, courbes)
├── Jupiter/ # Notebooks et scripts Python
│ ├── TP_IA_EMBARQUEE.ipynb # Analyse complète et entraînement
│ ├── Communication_STM32_NN.py # Communication UART avec la STM32
│ └── Modèles (H5/TFLite) et données de test
└── evaluation_results.txt # Synthèse des performances                                 
