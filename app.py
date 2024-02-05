from flask import Flask
from routes.user_routes import user_routes
from routes.default_routes import default_routes
from domain.base import db
from dotenv import load_dotenv
from os import getenv

load_dotenv()

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{getenv('DB_USER')}:{getenv('DB_PASSWORD')}@{getenv('DB_HOST')}:{getenv('DB_PORT')}/{getenv('DB_NAME')}"
app.register_blueprint(user_routes)
app.register_blueprint(default_routes)
db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    # Run the app on host 0.0.0.0 to make it externally accessible
    app.run(host='0.0.0.0', port=8080, debug=True)
