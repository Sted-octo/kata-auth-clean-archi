from flask import Blueprint, request, jsonify
from app.dependencies import auth_controller

auth_bp = Blueprint('auth', __name__)

class AuthController:
    def __init__(self, authenticate_use_case, token_service):
        self.authenticate_use_case = authenticate_use_case
        self.token_service = token_service

    def authenticate(self, request_data):
        name = request_data.get('name')
        password = request_data.get('password')

        if self.authenticate_use_case.authenticate(name, password):
            token = self.token_service.generate_token()
            return jsonify(token=token), 200
        else:
            return jsonify(message="Unauthorized"), 401
        
@auth_bp.route('/api/auth', methods=['POST'])
def authenticate_endpoint():
    data = request.json
    return auth_controller.authenticate(data)

