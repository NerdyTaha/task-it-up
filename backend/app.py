from flask import Flask, render_template 

app = Flask(__name__)

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
