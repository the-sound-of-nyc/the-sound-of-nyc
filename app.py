from flask import Flask, render_template, request, session, redirect, url_for
import utils

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/frequency/<frequency>')
def frequency(frequency):
    return render_template("index.html",input=frequency)

@app.route('/genre/<genre>')
def frequency(genre):
    return render_template("index.html", input=genre)

@app.route('/person/<person>')
def frequency(person):
    return render_template("index.html", input=person)

@app.route('/music/<music>')
def frequency(music):
    return render_template("index.html", input=music)

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
