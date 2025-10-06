import os
from flask import Flask, render_template 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from backend.models import user, task

#instance or object of Flask- our App
app = Flask(__name__)

# inisde app object, set up key-value pairs in dictionary to use a databse
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#A key for maintaining sessions.
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY") 

#instance or object of SQL_Alchemy - database 
db = SQLAlchemy(app)
#instance or object of Flask_Bcrypt to access encryption methods
bcrypt = Bcrypt(app)
# create Flask migrate instance 
migrate = Migrate(app, db)

#route for the home page
@app.route("/")
def home():
    return render_template("sign-in.html")

#Route for sign-in page
#setting the endpoint as 'sign-in' rather than the default function name
#url_for() in flask uses endpoint names and not URL's.
@app.route("/sign-in", endpoint="sign-in")
def sign_in():
    return render_template("sign-in.html")

#Route for Register page
@app.route("/register")
def register():
    return render_template("register.html")

# run the app only when executed stand-alone as a script and not when imported as a module
if __name__ == "__main__":
    app.run(debug=True)
