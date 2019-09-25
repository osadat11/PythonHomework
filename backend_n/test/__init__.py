from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

def create_app(app_name='TASKS-VUE'):
    app = Flask(app_name,
    static_folder="./dist/static",
    template_folder="./dist")
    app.config.from_object('backend.config.BaseConfig')

    return app