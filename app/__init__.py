from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def home():
        return render_template("index.html")

    @app.route("/getuser", methods=["GET"])
    def getUser():
        return jsonify({'result': 'User Data'})

    @app.route("/getclub", methods=["GET"])
    def getClub():
        return jsonify({'result': 'Club Data'})

    return app
