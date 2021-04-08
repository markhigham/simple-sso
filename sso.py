from flask import jsonify
from sso_user import User
from flask import Flask, request, redirect

app = Flask(__name__)

current_user = User(email="test.user@example.com", first_name="Test", last_name="User")


@app.route("/o/authorize/")
def authorize():
    client_redirect_uri = request.args["redirect_uri"]

    redirect_uri = (
        f"{client_redirect_uri}?state=abcde&redirect_uri={client_redirect_uri}&code=any_old_code"
    )

    return redirect(redirect_uri, code=302)


@app.route("/o/token/", methods=["POST"])
def exchange_token():
    
    token = request.form.get("code")
    app.logger.debug(token)
    result = {"access_token": token, "token_type": "Bearer"}
    return jsonify(result)


@app.route("/api/v1/user/me/")
def get_user():
    return jsonify(current_user.to_json())


@app.route("/api/v1/user/set/", methods=["POST"])
def set_user():
    new_user = request.json

    if new_user.get("email"):
        current_user.email = new_user["email"]

    if new_user.get("email_user_id"):
        current_user.email_user_id = new_user["email_user_id"]

    if new_user.get("user_id"):
        current_user.user_id = new_user["user_id"]

    if new_user.get("first_name"):
        current_user.first_name = new_user["first_name"]

    if new_user.get("last_name"):
        current_user.last_name = new_user["last_name"]

    return jsonify(current_user.to_json())
