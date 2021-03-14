from flask import jsonify
from sso_user import User
from flask import Flask

app = Flask(__name__)

current_user = User()

@app.route('/o/authorize/')
def authorize():
    

    return jsonify(current_user.to_json())