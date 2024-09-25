# Nom du projet

// Description du projet à compléter ici

Comment utiliser ce projet ?
- Nettoyer le Dockerfile si GCC n'est pas nécessaire
- Mettre à jour la version de python si besoin
- Mettre à jour les git hooks avec `pre-commit autoupdate`
- Sources python à compléter dans ./src. L'app est dans ./src/fastapi_app, ne pas déplacer ce fichier
- Ajouter les dépendances dans requirements.in
- Générer requirements.txt : `pip install pip-tools` & run `pip-compile`
- Vérifier que l'API démarre bien :
  - `docker compose up --build api`
  - Open http://localhost:5010
