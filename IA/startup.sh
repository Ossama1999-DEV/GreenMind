#!/usr/bin/env bash
set -euo pipefail

# ╭───────────────────────────────╮
# │ ENVIRONMENT DIR/ENVRC SETUP   │
# ╰───────────────────────────────╯
if ! command -v direnv &> /dev/null; then
    echo "❌ direnv n'est pas installé. Installe-le avant de continuer."
    echo "   Exemple (Debian/WSL) : sudo apt install direnv"
    exit 1
fi

if [ ! -f ".envrc" ]; then
    echo "📄 Création de .envrc..."
    cat << 'EOF' > .envrc
layout python3
export VIRTUAL_ENV=$(pwd)/.venv
export PATH=$VIRTUAL_ENV/bin:$PATH
EOF
fi

mkdir -p .direnv

# Active direnv
direnv allow > /dev/null 2>&1
eval "$(direnv export bash)"

# ╭──────────────────────────────╮
# │ PYTHON VENV SETUP            │
# ╰──────────────────────────────╯
if [ ! -d ".venv" ]; then
    echo "🐍 Création de l'environnement virtuel..."
    python3 -m venv .venv
fi

# Activation silencieuse
source .venv/bin/activate

# ╭──────────────────────────────╮
# │ INSTALL DEPENDENCIES         │
# ╰──────────────────────────────╯
echo "📦 Installation des dépendances..."
pip install --upgrade pip wheel setuptools > /dev/null 2>&1

# Dépendances IA/ML
pip install numpy scikit-learn > /dev/null 2>&1

# MQTT pour communication Pi ↔ ESP32
pip install paho-mqtt > /dev/null 2>&1

# OpenCV (optionnel, pour la vision caméra si besoin plus tard)
# pip install opencv-python-headless > /dev/null 2>&1

# Charger si besoin requirements.txt du projet
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt > /dev/null 2>&1
fi

# Installer le package local s’il y a un setup.py
if [ -f "setup.py" ]; then
    echo "🔨 Installation du package local..."
    pip install -e . > /dev/null 2>&1
fi

# Si tu veux lancer une doc/app spécifique
if [ -f "Doc/app.py" ]; then
    echo "📖 Lancement de la documentation..."
    python3 Doc/app.py || true
fi

# ╭──────────────────────────────╮
# │ QUICK TEST                   │
# ╰──────────────────────────────╯
echo "🧪 Test rapide du modèle IA..."
python3 - << 'PYCODE'
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
X = np.array([[25,60,800],[22,70,600],[28,50,1000]])
y = np.array(["Tomate","Salade","Basilic"])
knn = KNeighborsClassifier(n_neighbors=3).fit(X,y)
print("🌱 Exemple prédiction:", knn.predict([[23,68,700]])[0])
PYCODE

echo "✅ Environnement prêt !"
