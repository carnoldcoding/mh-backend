from flask import Blueprint, jsonify, request
from app.skills.service import get_skill_data

skill = Blueprint('skill', __name__)

@skill.route('/get_skill')
def get_skill():
    skill_id = request.args.get('id')
    return jsonify(get_skill_data(skill_id))