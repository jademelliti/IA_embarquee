Ceci est le fruit du travail de Jade MELLITI et Alexandra BARON. 

# Rapport de Projet - IA Embarquée sur STM32

## Table des Matières
1. [Introduction](#introduction)
2. [Architecture du Projet](#architecture-du-projet)
3. [Développement du Modèle ML](#-développement-du-modèle-ml)
4. [Intégration sur STM32](#-intégration-sur-stm32)
5. [Analyse des Performances](#-analyse-des-performances)
6. [Prise de Recul](#-prise-de-recul)
7. [Conclusion](#-conclusion)

## Introduction
Ce projet vise à développer un un réseau de neurones en Python pour la maintenance prédictive et à le déployer sur une carte STM32L4R9 pour une application embarquée. 

## Architecture du Projet
Notre solution se compose de deux parties principales :
1. *Partie PC* : Développement et entraînement du modèle
2. *Partie Embarquée* : Déploiement sur STM32

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
└── READ.ME                                 # Ce document ! 
