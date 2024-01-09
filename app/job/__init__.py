# app/job/__init__.py

from flask import Blueprint

job = Blueprint("job", __name__)

from . import routes