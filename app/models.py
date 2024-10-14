# # models.py
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class Product(db.Model):
#     __tablename__ = 'products'

#     product_id = db.Column(db.Integer, primary_key=True)
#     product_name = db.Column(db.String(100), nullable=False)
#     product_price = db.Column(db.Float, nullable=False)
#     product_instock = db.Column(db.Integer, nullable=False)
#     category_id = db.Column(db.Integer, nullable=False)

#     def __repr__(self):
#         return f'<Product {self.product_name}>'



'''{
    "product_id":"001",
    "product_name":"Product1",
    "product_price":"500",
    "product_instock":"10",
    "category_id":"001"
}'''
