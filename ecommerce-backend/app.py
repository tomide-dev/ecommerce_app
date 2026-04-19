from flask import Flask
from flask_cors import CORS
import sys
import os

# 🔥 Fix Python path issue (VERY IMPORTANT)
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from models import db, bcrypt
from routes.products import product_bp
from routes.auth import auth_bp
from routes.orders import order_bp
from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required

print("APP STARTED")  # Debug

app = Flask(__name__)
CORS(app)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Production-safe config
app.config['ENV'] = 'production'
app.config['DEBUG'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret-key'

# Initialize extensions
db.init_app(app)
bcrypt.init_app(app)
jwt = JWTManager(app)

# Register routes
app.register_blueprint(product_bp)
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(order_bp)

# Test route
@app.route('/')
def home():
    return "E-commerce API Running 🚀"

# 🔐 Protected route
@app.route('/protected')
@jwt_required()
def protected():
    return {"message": "Access granted"}

# 🔥 PRINT ALL ROUTES (VERY IMPORTANT)
print("\nREGISTERED ROUTES:")
for rule in app.url_map.iter_rules():
    print(rule)

# Run app
if __name__ == '__main__':
    app.run()