from flask import Flask
from app.interfaces.controllers import auth_bp
from app.dependencies import auth_controller

app = Flask(__name__)
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(debug=True)
