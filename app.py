from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to Engineering 89 DevOps team"

@app.route("/welcome/")
def welcome():
    return render_template("welcome.html")

# create a decorator to route traffic to login page
# display 2 messages of your choice in form of h1 and h2
@app.route("/login/")
def login():
    return redirect(url_for("/welcome"))
#redirect(url_for("/welcome/")) # this will redirect the user to the welcome page

#if __name__ == "__main__":
#    app.run(debug=True)