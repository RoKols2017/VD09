from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from app import db

game_bp = Blueprint('game', __name__)

@game_bp.route('/')
@login_required
def index():
    return render_template("index.html")

@game_bp.route('/click')
@login_required
def click():
    current_user.clicks += 1
    db.session.commit()
    return redirect(url_for('game.index'))

@game_bp.route('/deploy')
@login_required
def deploy():
    return render_template("deploy_instructions.html")
