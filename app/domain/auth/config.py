from flask_wtf import CSRFProtect

from main import app

csrf = CSRFProtect(app)