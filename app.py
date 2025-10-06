import os
from flask import Flask, render_template
from backend.extensions import db, bcrypt, migrate
from backend.models import user, task

def create_app():
    #instance or object of Flask- our App
    app = Flask(
    __name__,
    template_folder="backend/templates",
    static_folder="backend/static"
    )

    # app object needs to have key-value pairs of env variables
    app.config.from_mapping(
        SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SECRET_KEY=os.getenv("SECRET_KEY")
    )

    # Initialize extensions.py with app
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    #Register all the routes
    @app.route("/")
    def home():
        return render_template("sign-in.html")

    #setting the endpoint as 'sign-in' rather than the default function name
    #url_for() in flask uses endpoint names and not URL's.
    @app.route("/sign-in", endpoint="sign-in")
    def sign_in():
        return render_template("sign-in.html")

    @app.route("/register")
    def register():
        return render_template("register.html")

    return app

# run the app only when executed stand-alone as a script and not when imported as a module
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
