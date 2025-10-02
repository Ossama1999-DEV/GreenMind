"""
train.py : entraînement d'un modèle kNN pour recommander des plantes
"""

from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import joblib


def main():
    # Jeu de données fictif (à enrichir avec de vraies données)
    X = np.array([
        [25, 60, 800],   # Tomate
        [22, 70, 600],   # Salade
        [28, 50, 1000],  # Basilic
        [24, 65, 750],   # Tomate
        [21, 75, 500],   # Salade
        [29, 55, 950],   # Basilic
    ])

    y = np.array([
        "Tomate", "Salade", "Basilic",
        "Tomate", "Salade", "Basilic"
    ])

    # Création et entraînement du modèle kNN
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X, y)

    # Sauvegarde du modèle
    joblib.dump(knn, "greenmind_model.pkl")
    print("✅ Modèle kNN entraîné et sauvegardé dans greenmind_model.pkl")


if __name__ == "__main__":
    main()
