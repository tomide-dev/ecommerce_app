from flask import Flask
from flask_cors import CORS
import sys
import os
import time
from sqlalchemy.exc import OperationalError

# 🔥 Fix Python path issue
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from models import db, bcrypt
from routes.products import product_bp
from routes.auth import auth_bp
from routes.orders import order_bp
from flask_jwt_extended import JWTManager, jwt_required

print("APP STARTED")  # Debug

app = Flask(__name__)

# =========================
# 🔧 CONFIGURATION
# =========================
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@db:5432/ecommerce'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['ENV'] = 'production'
app.config['DEBUG'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret-key'

# =========================
# 🔌 INITIALIZE EXTENSIONS
# =========================
db.init_app(app)          # ✅ ONLY ONCE
bcrypt.init_app(app)
jwt = JWTManager(app)
CORS(app)

# =========================
# 🛢️ DATABASE INIT (FIXED)
# =========================
with app.app_context():
    for i in range(10):
        try:
            db.create_all()
            print("✅ Database ready")
            break
        except OperationalError:
            print("⏳ Waiting for database...")
            time.sleep(3)

# =========================
# 🔗 REGISTER ROUTES
# =========================
app.register_blueprint(product_bp)
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(order_bp)

# =========================
# 🧪 TEST ROUTES
# =========================
@app.route('/')
def home():
    return "E-commerce API Running 🚀"

@app.route('/protected')
@jwt_required()
def protected():
    return {"message": "Access granted"}

# =========================
# 🔍 PRINT ROUTES (DEBUG)
# =========================
print("\nREGISTERED ROUTES:")
for rule in app.url_map.iter_rules():
    print(rule)

# =========================
# ▶️ RUN APP (for local only)
# =========================
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)