<<<<<<< HEAD
=======
# SmartTrans-AI
Application locale pour traduire automatiquement des documents. Permet d’uploader des fichiers (PDF, DOCX, TXT), détecte la langue source, traduit vers la langue souhaitée et permet de télécharger le fichier traduit.


>>>>>>> f00caf4e53cf6b7b8328b758a45663e654288332
# SmartTrans AI

Application locale de traduction automatique de documents.

## 🎯 Fonctionnalités

- Upload de fichiers (PDF, DOCX, TXT)
- Détection automatique de la langue
- Traduction vers la langue de votre choix
- Téléchargement du fichier traduit

## 🛠️ Installation

1. **Installer les dépendances :**
```bash
pip install -r requirements.txt
```

2. **Lancer l'application :**
```bash
python backend/main.py
```

3. **Accéder à l'application :**
Ouvrez votre navigateur et allez sur `http://localhost:8000`

## 📁 Formats supportés

- **PDF** (.pdf)
- **Word** (.docx)
- **Texte** (.txt)

## 🚀 Utilisation

1. Sélectionnez un fichier à traduire
2. Cliquez sur "Analyser" pour détecter la langue
3. Choisissez la langue de destination
4. Cliquez sur "Traduire" pour générer le fichier traduit
5. Téléchargez le fichier traduit

## 🏗️ Architecture

```
SmartTransAI/
├── backend/
│   ├── main.py                # Application FastAPI
│   ├── utils/
│   │   ├── detect_language.py # Détection de langue
│   │   ├── translate.py       # Traduction
│   │   ├── file_reader.py    # Lecture de fichiers
│   │   └── file_writer.py    # Écriture de fichiers
│   └── templates/
│       └── index.html        # Interface utilisateur
├── temp/                     # Fichiers temporaires
├── requirements.txt
└── README.md
```

## 🔧 Technologies utilisées

- **Backend :** FastAPI, Python
- **Traduction :** Google Translate API
- **Détection de langue :** langdetect
- **Lecture PDF :** PyMuPDF
- **Lecture DOCX :** python-docx
- **Génération PDF :** FPDF2
<<<<<<< HEAD
- **Interface :** HTML + Bootstrap + Jinja2 
=======
- **Interface :** HTML + Bootstrap + Jinja2 
>>>>>>> f00caf4e53cf6b7b8328b758a45663e654288332
