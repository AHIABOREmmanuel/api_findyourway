# API FindYourWay

Cette API Flask sert de backend pour l'application FindYourWay, permettant la gestion des écoles et des formations.

## Prérequis

- Python 3.8 ou supérieur
- PostgreSQL 12 ou supérieur

## Installation

1. Créez un environnement virtuel Python :
```bash
python -m venv venv
```

2. Activez l'environnement virtuel :
- Windows :
```bash
venv\Scripts\activate
```
- Linux/Mac :
```bash
source venv/bin/activate
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

4. Créez une base de données PostgreSQL :
```sql
CREATE DATABASE findyourway_db;
```

5. Créez un fichier `.env` avec les variables suivantes :
```
PORT=5000
DATABASE_URL=postgresql://user:password@localhost:5432/findyourway_db
SECRET_KEY=your-secret-key-here
```

Note : Remplacez `user` et `password` par vos identifiants PostgreSQL.

## Démarrage de l'API

Pour lancer l'API en mode développement :
```bash
python app.py
```

L'API sera accessible à l'adresse : http://localhost:5000

## Points d'accès (Endpoints)

### Test de l'API
- GET `/api/test`
  - Retourne un message de test pour vérifier que l'API fonctionne

### Écoles
- GET `/api/schools/search?query=<recherche>`
  - Recherche des écoles par nom, spécialité ou description
  - Le paramètre `query` doit contenir au moins 3 caractères

- GET `/api/schools/<id>`
  - Récupère les détails d'une école spécifique

- POST `/api/schools`
  - Ajoute une nouvelle école
  - Corps de la requête (JSON) :
    ```json
    {
        "name": "Nom de l'école",
        "specialty": "Spécialité principale",
        "contact": "Informations de contact",
        "address": "Adresse complète",
        "description": "Description détaillée",
        "image": "URL de l'image",
        "technicalSheetUrl": "URL de la fiche technique",
        "testimonials": [
            {
                "author": "Nom de l'étudiant",
                "year": "2023",
                "content": "Témoignage"
            }
        ]
    }
    ```

- PUT `/api/schools/<id>`
  - Met à jour une école existante
  - Corps de la requête : même format que POST, tous les champs sont optionnels

- DELETE `/api/schools/<id>`
  - Supprime une école

### Points d'intérêt
- GET `/api/points-of-interest`
  - Récupère la liste des points d'intérêt
- POST `/api/points-of-interest`
  - Ajoute un nouveau point d'intérêt
  - Corps de la requête (JSON) :
    ```json
    {
        "name": "Nom du lieu",
        "latitude": 48.8584,
        "longitude": 2.2945,
        "description": "Description du lieu"
    }
    ``` 