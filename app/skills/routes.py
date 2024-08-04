from flask import Blueprint, jsonify
from app.skills.service import get_skill_data

skill = Blueprint('skill', __name__)

@skill.route('/get_skill')
def get_skill():
    return jsonify(get_skill_data())