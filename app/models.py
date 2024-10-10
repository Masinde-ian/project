# from flask import Flask, jsonify, request
# import pymysql

# app = Flask(__name__)

# from flask_restful import Resource, Api
# api = Api(app)

# class Product(Resource):
    
#     def get(self):
#         return jsonify({'message': 'hello world GET'})
    
#     def post(self):
#         data = request.json
#         product_id = data['product_id']
#         product_name = data['product_name']
#         product_price = data['product_price']
#         product_quantity = data['product_quantity']
#         product_category = data['product_category']

#         connection = pymysql.connect(host="localhost", user="root", password="", database="pos1")
#         cursor = connection.cursor()
#         sql = ''' insert into products (product_id, product_name, product_price, product_quantity, product_category) values (%s, %s, %s, %s, %s) '''
#         try:
#             cursor.execute(sql, (product_id, product_name, product_price, product_quantity, product_category))
#             connection.commit()
#             return jsonify({'message':'Post success, record saved'})

#         except:
#             connection.rollback
#             return jsonify({'message':'Post unsuccessful, record not saved'})


#     def delete(self):
#         return jsonify({'message': 'hello world DELETE'})
#     def put(self):
#         return jsonify({'message': 'hello world UPDATE'})
    
# api.add_resource(Product, '/products')

from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import pymysql

app = Flask(__name__)
api = Api(app)

class Product(Resource):
    
    def get(self):
        return jsonify({'message': 'hello world GET'})

    def post(self):
        data = request.json
        product_id = data['product_id']
        product_name = data['product_name']
        product_price = data['product_price']
        product_instock = data['product_instock']
        category_id = data['category_id']

        connection = pymysql.connect(host="localhost", user="root", password="", database="pos1")
        cursor = connection.cursor()
        sql = '''INSERT INTO product (product_id, product_name, product_price, product_instock, category_id) 
                 VALUES (%s, %s, %s, %s, %s)'''
        try:
            cursor.execute(sql, (product_id, product_name, product_price, product_instock, category_id))
            connection.commit()
            return jsonify({'message': 'Post success, record saved'}), 201
        except: 
            connection.rollback
            return jsonify({'message':'Post Failed, record not saved'})
        # except Exception as e:
        #     connection.rollback()
        #     return jsonify({'message': 'Post unsuccessful, record not saved', 'error': str(e)}), 500
        
        # finally:
        #     cursor.close()
        #     connection.close()

    def delete(self):
        return jsonify({'message': 'hello world DELETE'})

    def put(self):
        return jsonify({'message': 'hello world UPDATE'})

api.add_resource(Product, '/product')

if __name__ == '__main__':
    app.run(debug=True)


'''{
    "product_id":"001",
    "product_name":"Product1",
    "product_price":"500",
    "product_instock":"10",
    "category_id":"001"
}'''
