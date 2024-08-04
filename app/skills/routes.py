from flask import Blueprint, request, jsonify
from app.skills.service import get_skills

# Register Blueprint (Allows for modular routing)
skills = Blueprint("skills", __name__)

@skills.route("/get_skills", methods=['GET'])
def skill_info():
    return jsonify(get_skills())