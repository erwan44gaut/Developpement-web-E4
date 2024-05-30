from flask import Blueprint, request, jsonify, current_app
import hashlib
import utils.jwt_utils

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    payload = request.get_json()
    password = payload.get('password')

    # Convertir le mot de passe en hash md5
    hash_object = hashlib.md5(password.encode())
    password_hash = hash_object.hexdigest()

    # Comparer le hash du mot de passe fourni avec le hash stocké
    if password_hash == current_app.config['SECRET_KEY_HASH']:
        token = utils.jwt_utils.build_token()
        return jsonify({'token': token}), 200
    else:
        return 'Unauthorized', 401
