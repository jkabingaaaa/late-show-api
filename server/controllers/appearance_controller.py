from flask import Blueprint

appearance_bp = Blueprint('appearance_bp', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
def create_appearance():
    return {"message": "Appearance created"}