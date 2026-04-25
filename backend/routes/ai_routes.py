# backend/routes/ai_routes.py

from flask import Blueprint, request, jsonify
from controllers.ai_controller import get_room_suggestion

ai_bp = Blueprint("ai", __name__)

@ai_bp.route("/suggest-room", methods=["POST"])
def suggest_room():
    data = request.get_json()
    response, status = get_room_suggestion(data)
    return jsonify(response), status