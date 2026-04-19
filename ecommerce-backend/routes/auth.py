from flask import Blueprint, request, jsonify
from models import db, User
from flask_jwt_extended import create_access_token

print("AUTH FILE LOADED")  # 🔥 Debug (MUST SHOW)

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    print("REGISTER ENDPOINT HIT")  # Debug

    data = request.get_json()
    user = User(username=data['username'])
    user.set_password(data['password'])

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created"}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    print("LOGIN ENDPOINT HIT")  # Debug

    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()

    if user and user.check_password(data['password']):
        token = create_access_token(identity=user.id)
        return jsonify({"token": token})

    return jsonify({"message": "Invalid credentials"}), 401