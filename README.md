# 🌱 GreenMind

### 🏠 Maison

<img src="lab/serreMaison.png" alt="Serre connectée dans la maison" width="300"/>

### 🥕 Agroalimentaire

<img src="lab/serreAgro.png" alt="Serre connectée en agroalimentaire" width="300"/>

**GreenMind** est une serre intelligente pilotée par **IA**, développée dans le cadre du CESI.  
Le projet allie **ingénierie embarquée**, **agronomie** et **intelligence artificielle** pour automatiser la gestion d’une serre (arrosage, chauffage, capteurs, prévisions, etc.).


## 📁 Structure du projet

```
repo/GreenMind
├── AppMobile      # Application mobile (à venir)
├── AppWeb         # Interface web (dashboard)
├── doc            # Documentation technique
├── lab            # Prototypes & expérimentations
├── lib            # Bibliothèque interne (core)
│   ├── inc        # Headers publics
│   ├── src        # Sources
│   └── CMakeLists.txt
├── main           # Application principale (GreenMindApp)
├── test           # Tests unitaires (GoogleTest)
├── driver         # Artefacts générés (.a, .so, exécutable)
├── CMakeLists.txt # Build principal
├── startup.sh     # Script de build & packaging
└── README.md      # Ce fichier
```

## ⚙️ Build & Exécution

### 🔨 Compilation

Le projet utilise **CMake** et **GCC**.  
Toutes les étapes (configuration, compilation, génération des bibliothèques) sont automatisées via `startup.sh` :

```bash
./startup.sh
```

À la fin, le dossier `driver/` contient :
- l’exécutable `GreenMindApp`
- la bibliothèque statique `libGreenMindLib.a`
- la bibliothèque dynamique `libGreenMindLib.so`

### ▶️ Exécution

Lancer l’application principale :

```bash
./driver/GreenMindApp
```

Sortie attendue :
```
=== Bienvenue dans GreenMind ===
Version : GreenMind v0.1.0
```

## 🧪 Tests unitaires

Les tests unitaires sont gérés avec **GoogleTest** et intégrés au processus de build via `startup.sh`.

### Installation de GoogleTest (une seule fois)

Assurez-vous que les dépendances sont installées et que GoogleTest est compilé (nécessaire sur Debian/Ubuntu) :

```bash
sudo apt update
sudo apt install -y libgtest-dev cmake g++
cd /usr/src/gtest
sudo cmake .
sudo make -j$(nproc)
sudo cp lib/*.a /usr/lib
```

### Exécution des tests

Après compilation du projet, lancez les tests depuis le dossier `build` :

```bash
cd build
ctest --output-on-failure
```

Les résultats détaillés s’affichent en cas d’échec.  
Les tests couvrent la logique métier de la bibliothèque et de l’application principale.

## 🌐 Interface Web

Un prototype de dashboard est disponible dans `AppWeb/` :

- Affichage du logo et du nom GreenMind
- Curseur de luminosité
- Boutons pour ouvrir la porte et arroser

Pour lancer le dashboard :

```bash
cd AppWeb
python3 -m http.server 8080
```
Accéder à [http://localhost:8080](http://localhost:8080).

## 📦 Bibliothèques générées

Dans `driver/` :
- **Statique** : `libGreenMindLib.a`
- **Dynamique** : `libGreenMindLib.so`

Ces bibliothèques contiennent la logique interne réutilisable (mobile, web, services externes).

## 🗺️ Architecture du projet

```mermaid
flowchart LR
    Capteurs -- Données --> LibC++
    LibC++ -- API interne --> GreenMindApp
    GreenMindApp -- REST/API --> AppWeb
    GreenMindApp -- REST/API --> AppMobile
```

## 🚀 Prochaines étapes

- Ajouter les premiers capteurs (température, humidité, luminosité)
- Développer les modules de contrôle (chauffage, arrosage, ventilation)
- Intégrer le dashboard Web & Mobile avec la partie serveur
- Étendre les tests unitaires et fonctionnels
- Préparer une installation système (`make install`) pour distribuer la lib


## 👨‍💻 Auteurs

Projet développé par Équipe CESI:

- Chef de projet                : **DBIBIH Oussama**
- Responsables technique        : **Thomas Castello** & **Damien Navarri**
- Responsables business         : **Matthis Marti**
- Responsables communication    : **Quentin Hallier** & **Lucas Giraud**