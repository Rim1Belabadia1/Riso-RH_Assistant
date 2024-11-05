# Riso : Your IA RH Assistant
![WhatsApp Image 2024-07-12 à 04 22 58_3ff21427](https://github.com/user-attachments/assets/21eb51ad-df77-4b5c-8bfd-bd5557bf9295)
![WhatsApp Image 2024-07-12 à 04 22 58_b45a1915](https://github.com/user-attachments/assets/cdc45e5a-2832-4ac9-a338-a93f220b9d31)

## Description :

L'application **CV Interview App** est une application de gestion d'entretiens basée sur un CV. Elle permet aux utilisateurs de télécharger un CV (au format PDF), d'extraire son contenu et de générer automatiquement des questions et réponses basées sur ce CV à l'aide de l'IA. L'application permet également à l'utilisateur de générer des questions supplémentaires ou de personnaliser ses demandes de questions, et de copier les réponses générées dans le presse-papiers.

L'application se compose de deux pages principales :
- **Page de démarrage** : Une interface d'accueil avec un bouton pour démarrer l'application.
- **Page d'interface CV** : Permet de télécharger un CV, d'afficher des questions générées, et de personnaliser les demandes de questions.

## Fonctionnalités

- Téléchargement de CV en glisser-déposer ou via une fenêtre de sélection de fichier.
- Extraction du texte du CV et génération de questions et réponses.
- Génération de questions supplémentaires.
- Personnalisation des demandes de questions.
- Copie des questions et réponses dans le presse-papiers.
- Interface utilisateur moderne avec **CustomTkinter**.

## Prérequis

Avant de pouvoir exécuter l'application, assurez-vous d'avoir installé les bibliothèques suivantes :

- **Python 3.x** : L'application est développée en Python.
- **CustomTkinter** : Pour une interface graphique moderne.
- **TkinterDnD2** : Pour la fonctionnalité de glisser-déposer de fichiers.
- **pyperclip** : Pour copier du texte dans le presse-papiers.
- **Pillow** : Pour manipuler les images (utilisé dans le projet).

Vous pouvez installer les dépendances avec la commande suivante :


**pip install customtkinter tkinterdnd2 pyperclip Pillow**


## Installation

1. Clonez ce dépôt sur votre machine locale :
   
 
   **git clone https://github.com/votre-utilisateur/CV-Interview-App.git**

2. Accédez au répertoire du projet :
   

   **cd CV-Interview-App**


3. Installez les dépendances requises :


   **pip install -r requirements.txt**


4. Ajoutez les images nécessaires à votre répertoire de projet (par exemple `toph.PNG`, `lol.png`, `stat.png`).

## Utilisation

1. Lancer l'application en exécutant le fichier `start_page.py` :


   **python start_page.py**


2. Cliquez sur le bouton **Let's Start** pour accéder à la page principale de l'application **CV Interview App**.

3. Glissez-déposez un fichier CV (format PDF) dans la zone prévue à cet effet ou utilisez la fenêtre de sélection de fichiers pour le télécharger.

4. L'application générera des questions et réponses basées sur le contenu du CV téléchargé.

5. Utilisez les boutons pour copier les questions/réponses dans le presse-papiers ou pour générer des questions supplémentaires.

6. Vous pouvez également personnaliser les questions générées en fonction de votre demande spécifique.

## Structure du Projet


CV-Interview-App/
│
├── start_page.py           # Page de démarrage de l'application
├── interface.py            # Page principale de l'application CV Interview
├── aiml_generator.py       # Génération des questions et réponses avec AIML
├── cv_reader.py            # Lecture du fichier CV et extraction du texte
├── assets/                 # Répertoire contenant les images et autres ressources
│   ├── toph.PNG
│   ├── lol.png
│   └── stat.png
├── requirements.txt        # Liste des dépendances Python
└── README.md               # Ce fichier


## Auteurs

- **Rim Belabadia** - Développement de l'application



### Explications :
- **Prérequis** : Liste des dépendances que l'utilisateur doit installer pour faire fonctionner l'application.
- **Installation** : Instructions pour cloner le projet et installer les dépendances.
- **Utilisation** : Explication de la manière d'exécuter l'application et de son fonctionnement.
- **Structure du projet** : Organisation des fichiers du projet pour que l'utilisateur puisse s'y retrouver.
- **Auteurs** : Crédits au développeur du projet.
