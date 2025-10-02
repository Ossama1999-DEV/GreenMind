from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# === Jeu de données fictif (à enrichir avec de vraies données) ===
# [Température (°C), Humidité (%), Luminosité (lux)]
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

# === Création du modèle kNN ===
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

# === Exemple d’entrée (mesures capteurs de la serre) ===
# Remplace ces valeurs par tes capteurs en temps réel
sample = np.array([[23, 68, 700]])

# === Prédiction ===
prediction = knn.predict(sample)[0]
print(f"🌱 Plante conseillée : {prediction}")
