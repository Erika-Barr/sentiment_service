from flask import Flask, request
from flask_restful import Resource, Api
from flask_jsonpify import jsonify

app = Flask(__name__)
#api = Api(app)

#class Test(Resource):
#    def get(self):
#        test = 'this is a test'
#        return jsonify(test)


#api.add_resource(Test, '/test')

@app.route('/')
def index():
    return jsonify('test')

@app.route('/analyze/<twitter>')
def getTwitterHandle(twitter=None):
    ai_service = 'AI did a sentiment analysis on twitter handle: {}'.format(twitter)
    return jsonify(ai_service)


if __name__ == '__main__':
    #app.run(port='5002')
    app.run()
