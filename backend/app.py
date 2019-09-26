from flask import render_template
from api import app
# from .api import app
from flask_cors import CORS

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()