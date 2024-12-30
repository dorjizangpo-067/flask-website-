from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='tempaltes', static_folder='static')
    app.config["SECRITE_KEY"] = "dorjizangpo@1234"
    return app