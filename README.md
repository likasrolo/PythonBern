# 📰 Newsletter Personnalisée - Générateur IA

## 🎯 Vue d'ensemble

**Newsletter Personnalisée** est une application web moderne qui transforme vos newsletters et données clients en contenu personnalisé grâce à l'intelligence artificielle. L'application analyse automatiquement vos fichiers HTML de newsletter et vos données CRM Excel pour générer des prompts IA optimisés.

## ✨ Fonctionnalités

- **🔄 Interface Drag & Drop**: Téléchargement facile des fichiers HTML et Excel
- **🤖 Traitement IA Automatique**: Extraction et analyse intelligente des données
- **📊 Gestion des Sections**: Division automatique des clients en sections optimisées
- **💬 Génération de Prompts**: Création de prompts personnalisés pour l'IA
- **📋 Copie Automatique**: Copie directe des prompts dans le presse-papier
- **🎨 Interface Moderne**: Design responsive avec Bootstrap et animations
- **📈 Suivi de Progression**: Indicateurs visuels du traitement
- **💾 Sauvegarde Automatique**: Gestion des données et des résultats

## 🚀 Installation

### Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)
- Navigateur web moderne

### Installation rapide

1. **Cloner le repository** :
```bash
git clone <repository-url>
cd newsletter-app
```

2. **Installer les dépendances** :
```bash
pip install -r requirements.txt
```

3. **Lancer l'application** :
```bash
python run.py
```

4. **Ouvrir dans le navigateur** :
   - Accédez à : `http://localhost:5000`

## 🎮 Utilisation

### 1. **Téléchargement des fichiers**
- Glissez-déposez votre newsletter HTML
- Ajoutez votre fichier Excel CRM
- Cliquez sur "Lancer le traitement"

### 2. **Traitement des sections**
- Copiez les prompts générés automatiquement
- Collez-les dans votre outil IA (ChatGPT, Claude, etc.)
- Récupérez les réponses et collez-les dans l'interface
- Sauvegardez vos réponses

### 3. **Génération finale**
- Accédez à la page "Prompt Final"
- Générez le prompt de newsletter personnalisée
- Utilisez ce prompt pour créer votre newsletter finale

## 📁 Structure du projet

```
newsletter-app/
├── app.py                 # Application Flask principale
├── run.py                 # Fichier de démarrage
├── requirements.txt       # Dépendances Python
├── data/                  # Dossier de données (créé automatiquement)
├── templates/             # Templates HTML
│   ├── base.html         # Template de base
│   ├── index.html        # Page d'accueil
│   ├── sections.html     # Page des sections
│   └── final.html        # Page finale
├── static/               # Fichiers statiques
│   ├── css/style.css     # Styles personnalisés
│   └── js/app.js         # JavaScript commun
└── scr/                  # Modules de traitement
    ├── main.py           # Traitement principal
    ├── extract_html.py   # Extraction HTML
    └── extract_CRM_portfolio.py  # Traitement CRM
```

## 🔧 Configuration

### Variables d'environnement
```bash
export FLASK_ENV=development    # Mode développement
export FLASK_DEBUG=True         # Mode debug
```

### Formats de fichiers supportés
- **Newsletter** : `.html`, `.htm`
- **CRM** : `.xlsx`, `.xls`

## 🎨 Interface

L'application propose une interface moderne avec :
- **Design responsive** adapté à tous les écrans
- **Thème Bootstrap** avec animations fluides
- **Indicateurs de progression** visuels
- **Feedback utilisateur** en temps réel
- **Drag & Drop** intuitif

## 🔄 Workflow

1. **Upload** → Téléchargement des fichiers source
2. **Processing** → Traitement automatique des données
3. **Sections** → Génération et collecte des prompts par section
4. **Final** → Création du prompt final de newsletter

## 🛠️ Développement

### Lancer en mode développement
```bash
python app.py
```

### Structure des données
- `data/clients_sections.json` : Données clients organisées par sections
- `data/newsletter_md.md` : Newsletter convertie en Markdown
- `data/results_processed.json` : Résultats traités des réponses IA

## 🤝 Contribution

1. Fork le projet
2. Créer une branche feature (`git checkout -b feature/amelioration`)
3. Commit vos changements (`git commit -am 'Ajout nouvelle fonctionnalité'`)
4. Push sur la branche (`git push origin feature/amelioration`)
5. Créer une Pull Request

## 📄 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🆘 Support

Pour toute question ou problème :
- Créer une issue sur GitHub
- Consulter la documentation
- Vérifier les discussions existantes

## 🗺️ Roadmap

- [ ] 🌐 Support multilingue
- [ ] 🔗 Intégration API directe avec les IA
- [ ] 📱 Version mobile native
- [ ] 🔒 Authentification utilisateur
- [ ] 💾 Base de données pour la persistance
- [ ] 📊 Analytics et métriques avancées
- [ ] 🎯 Templates de newsletter prédéfinis


