from app import app
from models import db, Product

with app.app_context():
    p1 = Product(name="Laptop", price=1200)
    p2 = Product(name="Phone", price=800)

    db.session.add_all([p1, p2])
    db.session.commit()

    print("Products added!")
    