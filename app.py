from flask import Flask, render_template, request, session, redirect, url_for
import utils

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/frequency/<f>')
def frequency(f):
    return render_template("index.html")

@app.route('/genre/<g>')
def frequency(g):
    return render_template("index.html")

@app.route('/person/<p>')
def frequency(p):
    return render_template("index.html")

@app.route('/music/<m>')
def frequency(m):
    return render_template("index.html")

## Checks the username and password with the utils function auth()
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        userid = utils.auth(username, password)
        if userid != -1:
            session['logged_in'] = True
            session['userid'] = userid
            return redirect(url_for('home'))
        else:
            return render_template("login.html", err="Incorrect password or username")
    else:
        return render_template("login.html")

if __name__ == "__main__":
    app.debug = True
    # app.secret_key = "asdfghjkl"
    app.run('0.0.0.0',port=8000)
