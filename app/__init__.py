from flask import Flask
app = Flask(__name__)

from app import routes

# from flask_restful import Resource, Api
# api = Api(app)

# class Employee(Resource):
    
#     def get(self):
#         return jsonify({'message': 'hello world GET'})
    
#     def post(self):
#         return jsonify({'message': 'hello world POST'})
#     def delete(self):
#         return jsonify({'message': 'hello world DELETE'})
#     def put(self):
#         return jsonify({'message': 'hello world UPDATE'})
    
#     api.add_resource(Employee, '/employees')
    
# if __name__ == '__main__':
#     app.run(debug = True)
