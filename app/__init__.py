from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def home():
        return render_template("index.html")

    @app.route("/predict", methods=["GET"])
    def predict():
        # 1 laod image
        # 2 image -> tensor
        # prediction
        # return json

        return jsonify({'result': 'Welcome to KCF Hackathon'})

    return app
