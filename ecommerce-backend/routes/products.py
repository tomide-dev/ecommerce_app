from flask import Blueprint, jsonify
from models import Product
from flask_jwt_extended import jwt_required

product_bp = Blueprint('products', __name__)

@product_bp.route('/products')
@jwt_required()
def get_products():
    products = Product.query.all()
    return jsonify([
        {"id": p.id, "name": p.name, "price": p.price}
        for p in products
    ])