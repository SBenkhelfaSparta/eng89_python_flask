# Model View Controller - MVC - with Python Flask
## Python Flask
- Flask is a python micro-framework
- Flask is used to develop web apps
- Flask must first be installed in the app.py (using pip method), and an instance created
```python
from flask import Flask
app = Flask(__name__)
```
This is the basic structure of a Python file using Flask with 3 different webpages:
```python
@app.route("/")
def index():
    return "Welcome to Engineering 89 DevOps team"

@app.route("/welcome/")
def welcome():
    return "<h1>Welcome page for Flask app</h1>"

@app.route("/login/")
def login():
    return "<h1>Login</h1>" \
           "<h2>Enter your username</h2>"
```
- Error handing can be used to show a custom message/page when a page is unavailable
- flask contains redirect and url_for for this
```python
@app.route("/login/")
def login():
    return redirect(url_for("welcome"))
```
- This uses a HTML file to redirect from Python flask to .html file
## HTML
- HTML file:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Engineering 89 DevOps</title>
</head>
<body>
 <h1>The login page is unavailable.</h1>

</body>
</html>
```
## JavaScript
## Bootstrap
- getbootstrap.com contains many sections of code to help with designing pages
- e.g. navbar, login form
