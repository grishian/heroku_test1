from flask import Blueprint

bp_mushroom = Blueprint('bp_mushroom', __name__, cli_group="mushroom")

from . import views_mushroom
