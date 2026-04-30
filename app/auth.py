from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from .models import User
from . import db

auth = Blueprint("auth", __name__)


# REGISTER API
@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # user already exists check
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"msg": "User already exists"}), 400

    user = User(username=data['username'])
    user.set_password(data['password'])

    db.session.add(user)
    db.session.commit()

    return jsonify({"msg": "User registered successfully"})


# LOGIN API (REAL USER DB)
@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    user = User.query.filter_by(username=data['username']).first()

    if not user or not user.check_password(data['password']):
        return jsonify({"msg": "Invalid credentials"}), 401

    token = create_access_token(
    identity=str(user.id),
    additional_claims={"role": user.role}
)

    return jsonify({
        "msg": "Login successful",
        "token": token
    })