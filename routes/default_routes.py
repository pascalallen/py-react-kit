from flask import Blueprint, render_template

default_routes = Blueprint('default_routes', __name__)

@default_routes.route('/', defaults={'path': ''})
@default_routes.route('/<path:path>')
def default(path):
    return render_template('index.html')