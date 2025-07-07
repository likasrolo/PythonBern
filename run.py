#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fichier de démarrage pour l'application Newsletter Personnalisée

Usage:
    python run.py
"""

from app import app

if __name__ == '__main__':
    print("🚀 Démarrage de l'application Newsletter Personnalisée...")
    print("📱 Interface disponible sur: http://localhost:5000")
    print("💡 Appuyez sur Ctrl+C pour arrêter l'application")
    
    app.run(debug=True, host='0.0.0.0', port=5000)