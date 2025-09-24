from flask import Flask
from dotenv import load_dotenv
import os

from app.db.config import db, DB_URL
from app.controllers.music_controller import music_bp
from app.controllers.controller import index_bp
from app.controllers.auth.auth_controller import auth_bp

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
db.init_app(app)

app.register_blueprint(index_bp)
app.register_blueprint(music_bp)
app.register_blueprint(auth_bp)

app.run(debug=True)