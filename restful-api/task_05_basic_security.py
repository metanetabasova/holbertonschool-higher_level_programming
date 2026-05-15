#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity, get_jwt
)

app = Flask(__name__)

# tehlukesizlik ucun Secret key-ler
app.config['SECRET_KEY'] = 'super-secret-key'
app.config['JWT_SECRET_KEY'] + 'jwt-secret-key'

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# istifadeci melumatlari
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "user"
    }
}

# --- BASIC AUTH HISSESI ---
@auth.verify_password
def verify_password(username, password):
    ''' Basic Auth ucun istifadecini ve sifreni yoxlayir.'''
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username
    return None

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    '''Yalniz duzgun Basic Auth melumati olanlar daxil ola biler.'''
    return "Basic Auth: Access Granted"

# --- JWT AUTH HISSESI ---

@app.route('/login', methods=['POST'])
def login():
    '''Istifadeci adi ve sifre ile JWT token elde etmek ucun.'''
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get('username')
    password = data.get('password')

    user = users.get(username)
    if user and checj_password_hash(user['password'], password):
        # Rol melumatini tokenin icine yerlesdiririk
        access_token = create_access_token(
            identity=username,
            additional_claims={"role": user['role']}
        )
        return jsonify(access_token=access_token)

    return jsonify({"error": "Bad username or password"}), 401

@app.route('/jwt-protected')
@jwt_required()
def admin_only():
    '''Yalniz 'admin' rolu olanlar ucun.'''
    # Tokenin icindeki melumatlari oxuyuruq
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"

# --- JWT XETA IDAREEDICILERI ---

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.invalid_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

if __name__ ==  "__main__":
    app.run(hast='0.0.0.0', port=5000)
