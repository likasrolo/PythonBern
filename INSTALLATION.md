# 🚀 Guide d'Installation Rapide

## Prérequis
- Python 3.8+
- pip
- Navigateur web moderne

## Installation en 3 étapes

### 1. Installation des dépendances
```bash
pip install -r requirements.txt
```

### 2. Lancement de l'application
```bash
python run.py
```

### 3. Ouverture dans le navigateur
Ouvrez votre navigateur et allez sur : **http://localhost:5000**

## 🎯 Premier test

1. **Téléchargez vos fichiers** :
   - Newsletter HTML (via drag & drop)
   - Fichier Excel CRM

2. **Suivez le processus** :
   - Traitement automatique
   - Génération des prompts par section
   - Collecte des réponses IA
   - Génération du prompt final

## 🔧 Résolution de problèmes

### Erreur de dépendances
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### Port déjà utilisé
Modifiez le port dans `run.py` :
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Problème de permissions
Assurez-vous que le dossier `data/` peut être créé et écrit.

## 📞 Support
Si vous rencontrez des problèmes, vérifiez :
1. La version de Python (3.8+)
2. Les permissions d'écriture 
3. Les logs dans la console

Bon traitement de vos newsletters ! 🎉