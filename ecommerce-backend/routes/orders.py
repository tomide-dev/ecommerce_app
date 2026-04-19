from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Order

order_bp = Blueprint('orders', __name__)

@order_bp.route('/orders', methods=['POST'])
@jwt_required()
def create_order():
    user_id = get_jwt_identity()
    data = request.get_json()

    order = Order(user_id=user_id, total=data['total'])
    db.session.add(order)
    db.session.commit()

    return jsonify({"message": "Order created"})