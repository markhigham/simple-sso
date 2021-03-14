from flask import jsonify
from sso_user import User

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():

    u = User("mark@mark.com", "Mark", "Higham")

    return jsonify(u.to_json())