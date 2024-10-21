#run.py
from app import app
import pymysql
from datetime import datetime

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

class Order(Resource):

    def get(self):
        connection = pymysql.connect(host='localhost', user='root', password='',database='pos1')
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sql = "select * from purchase"
        cursor.execute(sql)
        if cursor.rowcount == 0:
            return jsonify({'message': 'No Records'})
        else:
            products = cursor.fetchall()
            return jsonify(products)

    def post(self):
        connection = pymysql.connect(host='localhost', user='root', password='', database='pos1')
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        data = request.json
        # Fetch the last purchase_id and increment it
        sql = "SELECT MAX(purchase_id) AS max_purchase_id FROM purchase"
        cursor.execute(sql)
        last_purchase = cursor.fetchone()
        purchase_id = (last_purchase['max_purchase_id'] + 1) if last_purchase['max_purchase_id'] is not None else 1  # Start from 1 if no records exist

        # purchase_id = data['purchase_id']
        product_name = data['product_name']

        # Fetch product id based on product name
        sql = "SELECT product_id FROM product WHERE product_name = %s"
        cursor.execute(sql, (product_name,))
        product = cursor.fetchone()
        if not product:
            connection.close()
            return jsonify({'message': 'Product not found'}), 404
        product_id = product['product_id']

        quantity  = data['quantity']
        unit_price = data['unit_price']
        total_price = unit_price * quantity
        # sale_date = datetime.now().strftime('%Y-%m-%d')
        date_ordered = datetime.now().strftime('%Y-%m-%d')
        # connection = pymysql.connect(host='localhost', user='root', password='',database='pos1')
        # cursor = connection.cursor()
        sql = "insert into purchase (purchase_id, product_name, product_id, quantity, unit_price, total_price, date_ordered) values(%s, %s, %s, %s, %s, %s, %s)"
        try:
            cursor.execute(sql, (purchase_id, product_name, product_id, quantity, unit_price, total_price, date_ordered))
            connection.commit()
            return jsonify({'message': 'POST SUCCESS. RECORD SAVED'})
        except:
            connection.rollback()
            return jsonify({'Error: There was a problem'})

    def delete(self):
        data = request.json
        purchase_id = data['purchase_id']
        connection = pymysql.connect(host='localhost', user='root', password='',database='pos1')
        cursor = connection.cursor()
        sql = "delete from purchase where product_id = %s"
        try:
            cursor.execute(sql, (purchase_id))
            connection.commit()
            return jsonify({'message': 'DELETE SUCCESS'})
        except:
            connection.rollback()
            return jsonify({'message': 'DELETE FAILED'})

    def put(self):
        data = request.json
        purchase_id = data['purchase_id']
        salary = data['salary']
        connection = pymysql.connect(host='localhost', user='root', password='',database='pos1')
        cursor = connection.cursor()
        sql = "update purchase SET quantity = %s where purchase_id =%s"
        try:
            cursor.execute(sql, (product_instock, product_id))
            connection.commit()
            return jsonify({'message': 'UPDATE SUCCESS'})
        except:
            connection.rollback()
            return jsonify({'message': 'UPDATE FAILED'})
api.add_resource(Order, '/orders')

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

class Sales(Resource):
    def get(self):
        connection = pymysql.connect(host='localhost', user='root', password='', database='pos1')
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM sale"
        cursor.execute(sql)
        sales = cursor.fetchall()
        connection.close()
        if not sales:
            return jsonify({'message': 'No Records'})
        return jsonify(sales)

    def post(self):
        data = request.json
        product_name = data['product_name']
        product_quantity = data['product_quantity']

        # Fetch product price based on product name
        connection = pymysql.connect(host='localhost', user='root', password='', database='pos1')
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT product_id, product_price, product_instock FROM product WHERE product_name = %s"
        cursor.execute(sql, (product_name,))
        product = cursor.fetchone()

        if not product:
            connection.close()
            return jsonify({'message': 'Product not found'}), 404

        product_id = product['product_id']
        product_price = product['product_price']
        total_paid = product_price * product_quantity

        current_instock = product['product_instock']
        new_instock = current_instock - product_quantity
        # Update the product_instock if there is enough stock
        if new_instock > 20:
            update_sql = "UPDATE product SET product_instock = %s WHERE product_id = %s"
            cursor.execute(update_sql, (new_instock, product_id))
            return jsonify("Stock updated successfully!")
        elif new_instock >=0:
            update_sql = "UPDATE product SET product_instock = %s WHERE product_id = %s"
            cursor.execute(update_sql, (new_instock, product_id))
            return jsonify(f"Make sure to update your stock, you are left with: {current_instock}, instock")
        else:
            return jsonify(f"Insufficient stock for product_id {product_id}. Current stock: {current_instock}, attempted to reduce by {quantity}.")

        # Fetch the last sale_id and increment it
        sql = "SELECT MAX(sale_id) AS max_sale_id FROM sale"
        cursor.execute(sql)
        last_sale = cursor.fetchone()
        sale_id = (last_sale['max_sale_id'] + 1) if last_sale['max_sale_id'] is not None else 1  # Start from 1 if no records exist

        # Get the current timestamp
        # current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sale_date = datetime.now().strftime('%Y-%m-%d')

        sql = "INSERT INTO sale (sale_id, product_name, product_id, product_price, product_quantity, total_paid, sale_date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        try:
            cursor.execute(sql, (sale_id, product_name, product_id, product_price, product_quantity, total_paid, sale_date))
            connection.commit()
            return jsonify({'message': 'POST SUCCESS. SALE RECORDED', 'sale_id': sale_id})
        except Exception as e:
            connection.rollback()
            return jsonify({'Error': str(e)})
        # finally:
        #     connection.close()

    def delete(self):
        data = request.json
        sale_id = data['sale_id']
        connection = pymysql.connect(host='localhost', user='root', password='', database='pos1')
        cursor = connection.cursor()
        sql = "DELETE FROM sale WHERE sale_id = %s"
        try:
            cursor.execute(sql, (sale_id,))
            connection.commit()
            return jsonify({'message': 'DELETE SUCCESS'})
        except:
            connection.rollback()
            return jsonify({'message': 'DELETE FAILED'})
        finally:
            connection.close()

    def put(self):
        data = request.json
        sale_id = data['sale_id']
        product_quantity = data['product_quantity']
        connection = pymysql.connect(host='localhost', user='root', password='', database='pos1')
        cursor = connection.cursor()
        sql = "UPDATE sale SET product_quantity = %s WHERE sale_id = %s"
        try:
            cursor.execute(sql, (product_quantity, sale_id))
            connection.commit()
            return jsonify({'message': 'UPDATE SUCCESS'})
        except:
            connection.rollback()
            return jsonify({'message': 'UPDATE FAILED'})
        finally:
            connection.close()
api.add_resource(Sales, '/saless')

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