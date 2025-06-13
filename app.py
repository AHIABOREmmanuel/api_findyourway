from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os
from models import School, Session, init_db
from sqlalchemy import or_

# Chargement des variables d'environnement
load_dotenv()

# Initialisation de l'application Flask
app = Flask(__name__)
CORS(app)  # Activation de CORS pour permettre les requêtes depuis le frontend Vue.js

# Initialisation de la base de données
init_db()

# Route de test
@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({"message": "API FindYourWay fonctionne correctement!"})

# Route pour rechercher des écoles
@app.route('/api/schools/search', methods=['GET'])
def search_schools():
    query = request.args.get('query', '').lower()
    session = Session()
    try:
        if not query:
            return jsonify([])
        
        schools = session.query(School).filter(
            or_(
                School.name.ilike(f'%{query}%'),
                School.specialty.ilike(f'%{query}%'),
                School.description.ilike(f'%{query}%')
            )
        ).all()
        return jsonify([school.to_dict() for school in schools])
    finally:
        session.close()

# Route pour obtenir les détails d'une école
@app.route('/api/schools/<int:school_id>', methods=['GET'])
def get_school(school_id):
    session = Session()
    try:
        school = session.query(School).get(school_id)
        if school is None:
            return jsonify({"error": "École non trouvée"}), 404
        return jsonify(school.to_dict())
    finally:
        session.close()

# Route pour ajouter une nouvelle école
@app.route('/api/schools', methods=['POST'])
def add_school():
    data = request.json
    session = Session()
    try:
        new_school = School(
            name=data['name'],
            specialty=data['specialty'],
            contact=data.get('contact', ''),
            address=data.get('address', ''),
            description=data.get('description', ''),
            image=data.get('image', ''),
            technical_sheet_url=data.get('technicalSheetUrl', ''),
            
        )
        session.add(new_school)
        session.commit()
        return jsonify(new_school.to_dict()), 201
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        session.close()

# Route pour mettre à jour une école
@app.route('/api/schools/<int:school_id>', methods=['PUT'])
def update_school(school_id):
    data = request.json
    session = Session()
    try:
        school = session.query(School).get(school_id)
        if school is None:
            return jsonify({"error": "École non trouvée"}), 404
        
        school.name = data.get('name', school.name)
        school.specialty = data.get('specialty', school.specialty)
        school.contact = data.get('contact', school.contact)
        school.address = data.get('address', school.address)
        school.description = data.get('description', school.description)
        school.image = data.get('image', school.image)
        school.technical_sheet_url = data.get('technicalSheetUrl', school.technical_sheet_url)
        
        session.commit()
        return jsonify(school.to_dict())
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        session.close()

# Route pour supprimer une école
@app.route('/api/schools/<int:school_id>', methods=['DELETE'])
def delete_school(school_id):
    session = Session()
    try:
        school = session.query(School).get(school_id)
        if school is None:
            return jsonify({"error": "École non trouvée"}), 404
        
        session.delete(school)
        session.commit()
        return jsonify({"message": "École supprimée avec succès"})
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        session.close()

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True) 