# 🤝 Guide de contribution à GreenMind

Merci de votre intérêt pour contribuer à **GreenMind** 🌱.  
Ce document décrit les bonnes pratiques et le workflow Git à respecter pour maintenir un projet propre et stable.

---

## 🔀 Stratégie de branches

- **`main`** : Branche stable, utilisée uniquement pour les versions validées.  
    *Seul l’administrateur du dépôt peut fusionner sur `main`.*

- **`dev`** : Branche d’intégration, utilisée pour tester et regrouper les contributions.  
    *Aucun commit direct n’est autorisé. Toutes les modifications doivent passer par des **Merge Requests / Pull Requests**.*

- **`feature/`** : Chaque contributeur doit créer sa propre branche de travail à partir de `dev`.  
    *Exemple : `feature/ajout-capteur-humidite`*

---

## 📌 Règles de contribution

1. **Créer une branche de travail depuis `dev` :**
     ```bash
     git checkout dev
     git pull origin dev
     git checkout -b feature/ma-fonctionnalite
     ```
2. **Développer et committer librement dans cette branche.**
3. **Respecter la structure du projet** (`lib/`, `main/`, `test/`, etc.).
4. **Suivre une convention de commit claire** (ex : `feat: ajout capteur humidité`).
5. **Lancer les tests avant toute demande de merge :**
     ```bash
     ./startup.sh
     cd build
     ctest --output-on-failure
     ```
     *Le merge vers `dev` est interdit si les tests échouent.*
6. **Créer une Merge Request (ou Pull Request) vers `dev`.**
7. **Décrire clairement les changements apportés.**
8. **Attendre validation (review + tests).**

---

## 🚦 Validation et merge

- **Seule l’intégration via MR/PR est autorisée.**
- **Interdiction de pousser directement dans `dev`.**
- **Merge vers `main` réservé à l’administrateur du dépôt, uniquement après validation complète des tests et revue finale.**
- **Utilisé pour préparer une version stable/release.**

---

## 🚫 Règles strictes

- ❌ Interdiction de merger directement dans `dev` sans MR/PR.
- ❌ Interdiction absolue de merger dans `main` sans autorisation explicite de l’administrateur.
- ❌ Tout code non testé ou non documenté sera refusé.

---

## ✅ Bonnes pratiques

- Mettre à jour régulièrement `dev` avant de pousser une nouvelle feature :
    ```bash
    git checkout dev
    git pull origin dev
    git checkout feature/ma-fonctionnalite
    git rebase dev
    ```
- Ajouter des tests unitaires pour chaque nouvelle fonctionnalité dans `test/`.
- Documenter les nouvelles fonctionnalités (`README`, `doc/`).
- Garder les commits clairs et atomiques.

---

## 👨‍💻 Workflow résumé

1. Créer branche → `feature/...` depuis `dev`
2. Coder + Commit → dans la branche
3. Tester → `startup.sh` + `ctest` doivent être verts ✅
4. Merge Request vers `dev` → revue + validation
5. Merge vers `main` → uniquement par l’admin

---

Merci de respecter ces règles 🙏 pour garantir la qualité et la stabilité de GreenMind 🌱
