# app/profil/__init__.py

from flask import Blueprint

profil = Blueprint("profil", __name__)

from . import routes