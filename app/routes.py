from flask import Blueprint, render_template, request, jsonify
from . import mongo
from bson import ObjectId

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/admin/')
def admin_home():
    return render_template('home.html')

