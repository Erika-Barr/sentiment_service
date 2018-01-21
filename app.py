from flask import Flask, request
from flask_restful import Resource, Api
from flask_jsonpify import jsonify
from sentimentService import getSentimentAnalysis

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify('test')

@app.route('/analyze/<twitter>')
def getTwitterHandle(twitter=None):
    ai_service = getSentimentAnalysis(twitter)
    return jsonify(ai_service)


if __name__ == '__main__':
    app.run()
