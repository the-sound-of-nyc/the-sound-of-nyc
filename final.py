from flask import Flask, render_template, request, session, redirect, url_for
import utils
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

#users = {}

# class Magic(Resource):
#     def get(self, user_id):
#         return {user_id: users[user_id]}
#
#     def put(self, user_id):
#         users[user_id][0] = request.form['f'] # 'frequency'
#         users[user_id][1] = request.form['g'] # 'genre'
#         users[user_id][2] = request.form['d'] # 'demographics'
#         users[user_id][3] = request.form['s'] # 'sound_file'
#
#         return {user_id: hello[user_id][0],
#                 user_id: hello[user_id][1],
#                 user_id: hello[user_id][2],
#                 user_id: hello[user_id][3]}#{user_id: users[user_id]}
#
# api.add_resource(Magic, '/<user_id>')

hello = {}

class Frequency(Resource):
    def get(self, user_id):
        return {user_id: hello[user_id]}

    def put(self, user_id):
        hello[user_id] = request.form['freq']
        return {user_id: hello[user_id]}

class Genre(Resource):
    def get(self, user_id):
        return {user_id: hello[user_id]}

    def put(self, user_id):
        hello[user_id] = request.form['genre']
        return {user_id: hello[user_id]}

class People(Resource):
    def get(self, user_id):
        return {user_id: hello[user_id]}

    def put(self, user_id):
        hello[user_id] = request.form['people']
        return {user_id: hello[user_id]}

class Sound(Resource):
    def get(self, user_id):
        return {user_id: hello[user_id]}

    def put(self, user_id):
        hello[user_id] = request.form['sound']
        return {user_id: hello[user_id]}
        
api.add_resource(Frequency, '/<user_id>')
api.add_resource(Genre, '/<user_id>')
api.add_resource(People, '/<user_id>')
api.add_resource(Sound, '/<user_id>')


# # api.add_resource(HelloWorld, '/<frequency>')
#
# # @app.route("/")
# # def home():
# #     return render_template("index.html")
#
# # @app.route('/frequency/<int:frequency>')
# # def frequency(frequency):
# #     return render_template("index.html",input=frequency)
#
# @app.route('/genre/<genre>')
# def genre(genre):
#     return render_template("index.html", input=genre)
#
# @app.route('/person/<person>')
# def person(person):
#     return render_template("index.html", input=person)
#
# @app.route('/music/<music>')
# def music(music):
#     return render_template("index.html", input=music)

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
