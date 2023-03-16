# Übernommen aus den Beispielen
import json
from app import app, db
from app.models import Users, ToDos, Updates
from flask import url_for, jsonify, request, abort
from flask_httpauth import HTTPTokenAuth

# Übernommen aus den Beispielen
token_auth = HTTPTokenAuth()

# Übernommen aus den Beispielen
@token_auth.verify_token
def verify_token(token):
    return Users.check_token(token) if token else None

# Eigenentwicklung
@app.route('/api/todo/<id>', methods=['GET'])
@token_auth.login_required
def get_todo(id):
    data = ToDos.query.get_or_404(id).json_one()
    return jsonify(data)

# Eigenentwicklung
@app.route('/api/todos', methods=['GET'])
@token_auth.login_required
def get_todos():
    data = ToDos.json_all()
    return jsonify(data)

# Eigenentwicklung
@app.route('/api/user/<id>', methods=['GET'])
@token_auth.login_required
def get_user(id):
    data = Users.query.get_or_404(id).json_one()
    return jsonify(data)

# Eigenentwicklung
@app.route('/api/users', methods=['GET'])
@token_auth.login_required
def get_users():
    data = Users.json_all()
    return jsonify(data)

# Eigenentwicklung
@app.route('/api/update/<id>', methods=['GET'])
@token_auth.login_required
def get_update(id):
    data = Updates.query.get_or_404(id).json_one()
    return jsonify(data)

# Eigenentwicklung
@app.route('/api/updates', methods=['GET'])
@token_auth.login_required
def get_updates():
    data = Updates.json_all()
    return jsonify(data)