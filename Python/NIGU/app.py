from flask import Flask, request, jsonify

from entities.user import User
from usecases.authentication.user_authentication import UserAuthentication

app = Flask(__name__)


@app.route('/api/auth', methods=['POST'])
def auth():
    data = request.json
    user = User(data["name"], data["password"])
    try:
        token = UserAuthentication.login(user)
        return jsonify(msg=token, code=200)
    except Exception as e:
        return jsonify(msg=type(e).__name__, code=401)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
