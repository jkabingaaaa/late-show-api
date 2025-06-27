from flask import Blueprint

guest_bp = Blueprint('guest_bp', __name__)

@guest_bp.route('/guests', methods=['GET'])
def list_guests():
    return {"guests": []}