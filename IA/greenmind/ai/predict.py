"""
predict.py : prédiction avec le modèle kNN
"""

import joblib
import numpy as np


def main():
    # Charger le modèle entraîné
    knn = joblib.load("greenmind_model.pkl")

    # Exemple de valeurs capteurs (à remplacer par MQTT ou capteurs réels)
    # cas 1 : Température=23°C, Humidité=68%, Luminosité=700 lux
    # sample = np.array([[23, 68, 700]])
    # cas 2 : Température=27°C, Humidité=55%, Luminosité=900 lux
    # sample = np.array([[27, 55, 900]])
    # cas 3 : Température=21°C, Humidité=75%, Luminosité=500 lux
    sample = np.array([[21, 75, 500]])
    # cas 4 : Température=30°C, Humidité=50%, Luminosité=1000 lux
    # sample = np.array([[30, 50, 1000]])

    prediction = knn.predict(sample)[0]
    print(f"🌱 Plante conseillée : {prediction}")


if __name__ == "__main__":
    main()
