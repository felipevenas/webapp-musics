from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

DB_SGBD = os.getenv('DB_SGBD')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')

DB_URL = f"{DB_SGBD}://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

db = SQLAlchemy()