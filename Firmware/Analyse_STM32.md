Analyzing model 
C:/Users/Alexandra/STM32Cube/Repository/Packs/STMicroelectronics/X-CUBE-AI/10.0.0/Utilities/windows/stedgeai.exe analyze --target stm32l4 --name ia_embarque -m C:/Users/Alexandra/Desktop/S8/IA MANUFACTURING/IA_emabrque_avec_jade/IA_embarquee/Jupiter/my_mlp_model.tflite --compression none --verbosity 1 --workspace C:/Users/ALEXAN~1/AppData/Local/Temp/mxAI_workspace2847865453630015774745826494843963 --output C:/Users/Alexandra/.stm32cubemx/ia_embarque_output 
ST Edge AI Core v2.0.0-20049 
Creating c (debug) info json file C:\Users\ALEXAN~1\AppData\Local\Temp\mxAI_workspace2847865453630015774745826494843963\ia_embarque_c_info.json 
  
 Exec/report summary (analyze) 
 --------------------------------------------------------------------------------------------------------------------------------------- 
 model file         :   C:\Users\Alexandra\Desktop\S8\IA MANUFACTURING\IA_emabrque_avec_jade\IA_embarquee\Jupiter\my_mlp_model.tflite    
 type               :   tflite                                                                                                           
 c_name             :   ia_embarque                                                                                                      
 compression        :   none                                                                                                             
 options            :   allocate-inputs, allocate-outputs                                                                                
 optimization       :   balanced                                                                                                         
 target/series      :   stm32l4                                                                                                          
 workspace dir      :   C:\Users\ALEXAN~1\AppData\Local\Temp\mxAI_workspace2847865453630015774745826494843963                            
 output dir         :   C:\Users\Alexandra\.stm32cubemx\ia_embarque_output                                                               
 model_fmt          :   float                                                                                                            
 model_name         :   my_mlp_model                                                                                                     
 model_hash         :   0x58d2695a1214a2eda0fd5fb45178fa7f                                                                               
 params #           :   4,869 items (19.02 KiB)                                                                                          
 --------------------------------------------------------------------------------------------------------------------------------------- 
 input 1/1          :   'serving_default_ke.._tensor_90', f32(1x5), 20 Bytes, activations                                                
 output 1/1         :   'nl_4', f32(1x5), 20 Bytes, activations                                                                          
 macc               :   5,072                                                                                                            
 weights (ro)       :   19,476 B (19.02 KiB) (1 segment)                                                                                 
 activations (rw)   :   512 B (512 B) (1 segment) *                                                                                      
 ram (total)        :   512 B (512 B) = 512 + 0 + 0                                                                                      
 --------------------------------------------------------------------------------------------------------------------------------------- 
 (*) 'input'/'output' buffers can be used from the activations buffer 
Computing AI RT data/code size (target=stm32l4).. 
 Model name - my_mlp_model 
 ------ ----------------------------------- ------------- -------------- ------- -------------------------------- 
 m_id   layer (original)                    oshape        param/size        macc                     connected to 
 ------ ----------------------------------- ------------- -------------- ------- -------------------------------- 
 0      serving_default_ke.._tensor_90 ()   [b:1,c:5] 
        reshape_0 (RESHAPE)                 [b:1,c:5]                              serving_default_ke.._tensor_90 
 ------ ----------------------------------- ------------- -------------- ------- -------------------------------- 
 1      arith_constant2 ()                  [b:64,c:5]    320/1,280 
        arith_constant5 ()                  [b:64]        64/256 
        gemm_1 (FULLY_CONNECTED)            [b:1,c:64]                       384                        reshape_0 
                                                                                                  arith_constant2 
                                                                                                  arith_constant5 
        nl_1_nl (FULLY_CONNECTED)           [b:1,c:64]                        64                           gemm_1 
 ------ ----------------------------------- ------------- -------------- ------- -------------------------------- 
 2      arith_constant1 ()                  [b:64,c:64]   4,096/16,384 
        arith_constant4 ()                  [b:64]        64/256 
        gemm_2 (FULLY_CONNECTED)            [b:1,c:64]                     4,160                          nl_1_nl 
                                                                                                  arith_constant1 
                                                                                                  arith_constant4 
        nl_2_nl (FULLY_CONNECTED)           [b:1,c:64]                        64                           gemm_2 
 ------ ----------------------------------- ------------- -------------- ------- -------------------------------- 
 3      arith_constant ()                   [b:5,c:64]    320/1,280 
        arith_constant3 ()                  [b:5]         5/20 
        gemm_3 (FULLY_CONNECTED)            [b:1,c:5]                        325                          nl_2_nl 
                                                                                                   arith_constant 
                                                                                                  arith_constant3 
 ------ ----------------------------------- ------------- -------------- ------- -------------------------------- 
 4      nl_4 (SOFTMAX)                      [b:1,c:5]                         75                           gemm_3 
 ------ ----------------------------------- ------------- -------------- ------- -------------------------------- 
 model: macc=5,072 weights=19,476 activations=-- io=-- 
 Number of operations per c-layer 
 ------- ------ ------------------------ ------- -------------- 
 c_id    m_id   name (type)                  #op           type 
 ------- ------ ------------------------ ------- -------------- 
 0       1      gemm_1 (Dense)               384   smul_f32_f32 
 1       1      nl_1_nl (Nonlinearity)        64     op_f32_f32 
 2       2      gemm_2 (Dense)             4,160   smul_f32_f32 
 3       2      nl_2_nl (Nonlinearity)        64     op_f32_f32 
 4       3      gemm_3 (Dense)               325   smul_f32_f32 
 5       4      nl_4 (Nonlinearity)           75     op_f32_f32 
 ------- ------ ------------------------ ------- -------------- 
 total                                     5,072 
 Number of operation types 
 ---------------- ------- ----------- 
 operation type         #           % 
 ---------------- ------- ----------- 
 smul_f32_f32       4,869       96.0% 
 op_f32_f32           203        4.0% 
 Complexity report (model) 
 ------ ----------------- ------------------------- ------------------------- -------- 
 m_id   name              c_macc                    c_rom                     c_id 
 ------ ----------------- ------------------------- ------------------------- -------- 
 1      arith_constant2   ||                 8.8%   ||                 7.9%   [0, 1] 
 2      arith_constant1   ||||||||||||||||  83.3%   ||||||||||||||||  85.4%   [2, 3] 
 3      arith_constant    ||                 6.4%   ||                 6.7%   [4] 
 4      nl_4              |                  1.5%   |                  0.0%   [5] 
 ------ ----------------- ------------------------- ------------------------- -------- 
 macc=5,072 weights=19,476 act=512 ram_io=0 
 Requested memory size by section - "stm32l4" target 
 ------------------------------ ------- -------- ------- ----- 
 module                            text   rodata    data   bss 
 ------------------------------ ------- -------- ------- ----- 
 NetworkRuntime1000_CM4_GCC.a     7,012        0       0     0 
 ia_embarque.o                      534       48   1,752   148 
 ia_embarque_data.o                  48       16      88     0 
 lib (toolchain)*                   614       24       0     0 
 ------------------------------ ------- -------- ------- ----- 
 RT total**                       8,208       88   1,840   148 
 ------------------------------ ------- -------- ------- ----- 
 weights                              0   19,480       0     0 
 activations                          0        0       0   512 
 io                                   0        0       0     0 
 ------------------------------ ------- -------- ------- ----- 
 TOTAL                            8,208   19,568   1,840   660 
 ------------------------------ ------- -------- ------- ----- 
 *  toolchain objects (libm/libgcc*) 
 ** RT AI runtime objects (kernels+infrastructure) 
  Summary - "stm32l4" target 
  --------------------------------------------------- 
               FLASH (ro)      %*   RAM (rw)       % 
  --------------------------------------------------- 
  RT total         10,136   34.2%      1,988   79.5% 
  --------------------------------------------------- 
  TOTAL            29,616              2,500 
  --------------------------------------------------- 
  *  rt/total 
Creating txt report file C:\Users\Alexandra\.stm32cubemx\ia_embarque_output\ia_embarque_analyze_report.txt 
elapsed time (analyze): 9.996s 
Model file:      my_mlp_model.tflite 
Total Flash:     29612 B (28.92 KiB) 
    Weights:     19476 B (19.02 KiB) 
    Library:     10136 B (9.90 KiB) 
Total Ram:       2500 B (2.44 KiB) 
    Activations: 512 B 
    Library:     1988 B (1.94 KiB) 
    Input:       20 B (included in Activations) 
    Output:      20 B (included in Activations) 
Done 
Analyze complete on AI model