from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class UserAPI(Resource):
    def get(self, id):
        print('get with id', id)
        pass

    def put(self, id):
        print('put')
        pass

    def delete(self, id):
        print('delete')
        pass

api.add_resource(UserAPI, '/users/<int:id>', endpoint = 'user')