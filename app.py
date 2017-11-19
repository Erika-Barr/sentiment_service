from flask import Flask, request
from flask_restful import Resource, Api
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

class Test(Resource):
    def get(self):
        test = 'this is a test'
        return jsonify(test)


api.add_resource(Test, '/test')

if __name__ == '__main__':
    app.run(port='5002')
