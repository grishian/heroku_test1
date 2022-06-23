from flask import Blueprint

bp_temperature = Blueprint('bp_temperature', __name__, cli_group="temperature")

from . import views_temperature
