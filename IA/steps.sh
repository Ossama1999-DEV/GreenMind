# Crée l'environnement virtuel si pas déjà fait
python3 -m venv .venv
source .venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Installer ta lib en mode développement
pip install -e .

# Entraîner le modèle kNN
greenmind-train

# Lancer une prédiction
greenmind-predict


# Tester directement en Python
# python3 -m greenmind.ai.train
# python3 -m greenmind.ai.predict



