#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Istifadecileri yaddasda saxlamag ucun luget
users = {}

@app.route("/")
def home():
    '''Ana sehife'''
    return "Welcome to the Flask API!"

@app.route("/data")
def get_data():
    '''Butun movcud istifadeci adlarinin siyahisini JSON olaraq qaytarir.'''
    return jsonify(list(users.keys()))

@app.route("/status")
def get_status():
    '''API-in veziyyetini yoxlayir.'''
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    '''Konkret istifadeci haqqinda butun melumatlari qaytarir.'''
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    '''Yeni istifadeci elave etmek ucun post sorgusu.'''
    # JSON-u yoxlayiriq (silent=True xata vermesin deye)
    data = request.get_json(silent=True)
    
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    # Sert 1: Username mutleqdir
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Sert 2: Username artiq varsa xata ver (Conflict 409)
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Her sey qaydasindadirsa, lugete elave et
    users[username] = data
    
    # Ugurlu cavab qaytar (201 Created)
    return jsonify({"message": "User added", "user": data}), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
