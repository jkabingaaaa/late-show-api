from flask import Blueprint

episode_bp = Blueprint('episode_bp', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def list_episodes():
    return {"episodes": []}