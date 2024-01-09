# app/firm/__init__.py

from flask import Blueprint

firm = Blueprint("firm", __name__)

from . import routes