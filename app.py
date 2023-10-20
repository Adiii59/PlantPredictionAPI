from flask import Flask
from flask import render_template

app = None
def create_app():
    app = Flask(__name__, template_folder = "templates")
    app.app_context().push()
    return app

app = create_app()
@app.route("/")
def home():
    return render_template("index.html")


from api import *
