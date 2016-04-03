from flask import Flask, render_template, request, session, redirect, url_for
import utils
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

hello = {}

class Frequency(Resource):
    def get(self, user_id):
        return {user_id: hello[user_id]}

    def put(self, user_id):
        hello[user_id] = request.form['data']
        return {user_id: hello[user_id]}


api.add_resource(Frequency, '/<user_id>')

if __name__ == "__main__":
    app.debug = True
    # app.secret_key = "asdfghjkl"
    app.run('0.0.0.0',port=8000)
