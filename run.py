#run.py
from app import app
import pymysql
# if __name__ == "__main__":
#     app.run(debug = True)

from flask import Flask, jsonify, request
from flask_restful import Resource, Api
# app = Flask(__name__)
api = Api(app)

class Product(Resource):

    def get(self):
        connection = pymysql.connect(host='localhost', user='root', password='',database='pos1')
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sql = "select * from product"
        cursor.execute(sql)
        if cursor.rowcount == 0:
            return jsonify({'message': 'No Records'})
        else:
            products = cursor.fetchall()
            return jsonify(products)

    def post(self):
        data = request.json
        product_id = data['product_id']
        product_name = data['product_name']
        product_price = data['product_price']
        product_instock = data['product_instock']
        category_id = data['category_id']
        connection = pymysql.connect(host='localhost', user='root', password='',database='pos1')
        cursor = connection.cursor()
        sql = "insert into product (product_id, product_name, product_price, product_instock, category_id) values(%s, %s, %s, %s, %s)"
        try:
            cursor.execute(sql, (product_id, product_name, product_price, product_instock, category_id))
            connection.commit()
            return jsonify({'message': 'POST SUCCESS. RECORD SAVED'})
        except:
            connection.rollback()
            return jsonify({'Error: There was a problem'})

    def delete(self):
        data = request.json
        product_id = data['product_id']
        connection = pymysql.connect(host='localhost', user='root', password='',database='pos1')
        cursor = connection.cursor()
        sql = "delete from product where product_id = %s"
        try:
            cursor.execute(sql, (product_id))
            connection.commit()
            return jsonify({'message': 'DELETE SUCCESS'})
        except:
            connection.rollback()
            return jsonify({'message': 'DELETE FAILED'})

    def put(self):
        data = request.json
        product_id = data['Product_id']
        salary = data['salary']
        connection = pymysql.connect(host='localhost', user='root', password='',database='pos1')
        cursor = connection.cursor()
        sql = "update product SET product_instock = %s where product_id =%s"
        try:
            cursor.execute(sql, (product_instock, product_id))
            connection.commit()
            return jsonify({'message': 'UPDATE SUCCESS'})
        except:
            connection.rollback()
            return jsonify({'message': 'UPDATE FAILED'})
api.add_resource(Product, '/products')

class Category(Resource):

    def get(self):
        connection = pymysql.connect(host='localhost', user='root', password='',database='pos1')
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sql = "select * from category"
        cursor.execute(sql)
        if cursor.rowcount == 0:
            return jsonify({'message': 'No Records'})
        else:
            display = cursor.fetchall()
            return jsonify(display)

    def post(self):
        data = request.json
        category_id = data['category_id']
        category_name = data['category_name']
        
        connection = pymysql.connect(host='localhost', user='root', password='',database='pos1')
        cursor = connection.cursor()
        sql = "insert into category (category_id, category_name) values(%s, %s)"
        try:
            cursor.execute(sql, (category_id, category_name))
            connection.commit()
            return jsonify({'message': 'POST SUCCESS. RECORD SAVED'})
        except:
            connection.rollback()
            return jsonify({'Error: There was a problem'})

    def delete(self):
        data = request.json
        category_id = data['product_id']
        connection = pymysql.connect(host='localhost', user='root', password='',database='pos1')
        cursor = connection.cursor()
        sql = "delete from category where category_id = %s"
        try:
            cursor.execute(sql, (category_id))
            connection.commit()
            return jsonify({'message': 'DELETE SUCCESS'})
        except:
            connection.rollback()
            return jsonify({'message': 'DELETE FAILED'})

    def put(self):
        data = request.json
        category_id = data['category_id']
        salary = data['salary']
        connection = pymysql.connect(host='localhost', user='root', password='',database='pos1')
        cursor = connection.cursor()
        sql = "update category SET category_name = %s where category_id =%s"
        try:
            cursor.execute(sql, (category_name, category_id))
            connection.commit()
            return jsonify({'message': 'UPDATE SUCCESS'})
        except:
            connection.rollback()
            return jsonify({'message': 'UPDATE FAILED'})
api.add_resource(Category, '/categories')

class Sale(Resource):

    def get(self):
        connection = pymysql.connect(host='localhost', user='root', password='',database='HyraxEmpDB')
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sql = "select * from sale"
        cursor.execute(sql)
        if cursor.rowcount == 0:
            return jsonify({'message': 'No Records'})
        else:
            products = cursor.fetchall()
            return jsonify(products)

    def post(self):
        data = request.json
        sale_id = data['sale_id']
        product_name = data['product_name']
        product_id = data['product_id']
        product_price = data['product_price']
        product_quantity = data['product_quantity']
        total_paid = data['total_paid']
        connection = pymysql.connect(host='localhost', user='root', password='',database='pos1')
        cursor = connection.cursor()
        sql = "insert into sale (sale_id, product_name, product_id, product_price, product_quantity, total_paid) values(%s, %s, %s, %s, %s, %s)"
        try:
            cursor.execute(sql, (sale_id, product_name, product_id, product_price, product_quantity, total_paid))
            connection.commit()
            return jsonify({'message': 'POST SUCCESS. RECORD SAVED'})
        except:
            connection.rollback()
            return jsonify({'Error: There was a problem'})

    def delete(self):
        data = request.json
        sale_id = data['sale_id']
        connection = pymysql.connect(host='localhost', user='root', password='',database='pos1')
        cursor = connection.cursor()
        sql = "delete from sale where sale_id = %s"
        try:
            cursor.execute(sql, (sale_id))
            connection.commit()
            return jsonify({'message': 'DELETE SUCCESS'})
        except:
            connection.rollback()
            return jsonify({'message': 'DELETE FAILED'})

    def put(self):
        data = request.json
        sale_id = data['sale_id']
        product_quantity = data['product_quantity']
        connection = pymysql.connect(host='localhost', user='root', password='',database='pos1')
        cursor = connection.cursor()
        sql = "update sale SET product_quantity = %s where sale_id =%s"
        try:
            cursor.execute(sql, (product_quantity, sale_id))
            connection.commit()
            return jsonify({'message': 'UPDATE SUCCESS'})
        except:
            connection.rollback()
            return jsonify({'message': 'UPDATE FAILED'})
api.add_resource(Sale, '/sales')

class Transaction(Resource):

    def get(self):
        connection = pymysql.connect(host='localhost', user='root', password='',database='HyraxEmpDB')
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sql = "select * from transaction"
        cursor.execute(sql)
        if cursor.rowcount == 0:
            return jsonify({'message': 'No Records'})
        else:
            products = cursor.fetchall()
            return jsonify(products)

    def post(self):
        data = request.json
        transaction_id = data['transaction_id']
        sale_id = data['sale_id']
        total_paid = data['total_paid']
        customer_name = data['customer_name']
        connection = pymysql.connect(host='localhost', user='root', password='',database='pos1')
        cursor = connection.cursor()
        sql = "insert into transaction (transaction_id, sale_id, total_paid, customer_name) values(%s, %s, %s, %s)"
        try:
            cursor.execute(sql, (transaction_id, sale_id, total_paid, customer_name))
            connection.commit()
            return jsonify({'message': 'POST SUCCESS. RECORD SAVED'})
        except:
            connection.rollback()
            return jsonify({'Error: There was a problem'})

    def delete(self):
        data = request.json
        transaction_id = data['transaction_id']
        connection = pymysql.connect(host='localhost', user='root', password='',database='pos1')
        cursor = connection.cursor()
        sql = "delete from transaction where transaction_id = %s"
        try:
            cursor.execute(sql, (transaction_id))
            connection.commit()
            return jsonify({'message': 'DELETE SUCCESS'})
        except:
            connection.rollback()
            return jsonify({'message': 'DELETE FAILED'})

    # We don,t need this update function in this class
    """def put(self):
        data = request.json
        transaction_id = data['transaction_id']
        salary = data['salary']
        connection = pymysql.connect(host='localhost', user='root', password='',database='pos1')
        cursor = connection.cursor()
        sql = "update product SET product_instock = %s where product_id =%s"
        try:
            cursor.execute(sql, (product_instock, product_id))
            connection.commit()
            return jsonify({'message': 'UPDATE SUCCESS'})
        except:
            connection.rollback()
            return jsonify({'message': 'UPDATE FAILED'})"""
api.add_resource(Transaction, '/transactions')

class User(Resource):

    def get(self):
        connection = pymysql.connect(host='localhost', user='root', password='',database='HyraxEmpDB')
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sql = "select * from users"
        cursor.execute(sql)
        if cursor.rowcount == 0:
            return jsonify({'message': 'No Records'})
        else:
            products = cursor.fetchall()
            return jsonify(products)

    def post(self):
        data = request.json
        user_id = data['user_id']
        username = data['username']
        password_hash = data['password_hash']
        role = data['role']
        date_joined = data['date_joined']
        connection = pymysql.connect(host='localhost', user='root', password='',database='pos1')
        cursor = connection.cursor()
        sql = "insert into users (user_id, username, password_hash, role, date_joined) values(%s, %s, %s, %s, %s)"
        try:
            cursor.execute(sql, (user_id, username, password_hash, role, date_joined))
            connection.commit()
            return jsonify({'message': 'POST SUCCESS. RECORD SAVED'})
        except:
            connection.rollback()
            return jsonify({'Error: There was a problem'})

    def delete(self):
        data = request.json
        user_id = data['user_id']
        connection = pymysql.connect(host='localhost', user='root', password='',database='pos1')
        cursor = connection.cursor()
        sql = "delete from users where user_id = %s"
        try:
            cursor.execute(sql, (user_id))
            connection.commit()
            return jsonify({'message': 'DELETE SUCCESS'})
        except:
            connection.rollback()
            return jsonify({'message': 'DELETE FAILED'})

    def put(self):
        data = request.json
        user_id = data['user_id']
        password_hash = data['password_hash']
        connection = pymysql.connect(host='localhost', user='root', password='',database='pos1')
        cursor = connection.cursor()
        sql = "update users SET password_hash = %s where user_id =%s"
        try:
            cursor.execute(sql, (password_hash, user_id))
            connection.commit()
            return jsonify({'message': 'UPDATE SUCCESS'})
        except:
            connection.rollback()
            return jsonify({'message': 'UPDATE FAILED'})
api.add_resource(User, '/users')

if __name__ == '__main__':
    app.run(debug = True)