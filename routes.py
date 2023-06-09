
from flask import render_template, request, redirect, url_for, jsonify
from datetime import datetime, timedelta
from . import bp
import random
from flask_login import current_user

@bp.route('/fish_tank')
def fish_tank():
    fishes = Fish.query.filter_by(user_id=current_user.id).all()
    return render_template('fish_tank.jinja', fishes=fishes)

@bp.route('/api/fish', methods=['GET'])
def get_random_fish():
    fish_id = random.choice(list(fish_library.keys()))  
    fish_info = fish_library.get(fish_id)  
    if fish_info:
        return jsonify(fish_info)
    else:
        return jsonify({'error': 'Fish not found'})
