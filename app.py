from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/user_settings", methods=['GET'])
def get_user_settings():
    f = open('user_settings.json')
    data = json.load(f)
    return jsonify(data)

@app.route("/user_settings", methods=['POST'])
def post_user_settings():
    js_data  =  request.json
    with open('user_settings.json', 'w') as f:
        json.dump(js_data, f)

    return '', 200


@app.route("/mlops", methods=['GET'])
def get_mlops():
    f = open('mlops.json')
    data = json.load(f)
    return jsonify(data)

@app.route("/mlops", methods=['POST'])
def post_mlops():
    js_data  =  request.json
    with open('mlops.json', 'w') as f:
        json.dump(js_data, f)

    return '', 200