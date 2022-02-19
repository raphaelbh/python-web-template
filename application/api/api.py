from flask import Blueprint

from commons import api_utils
from services import fake_service

blueprint = Blueprint("api", __name__)

@blueprint.route('/demo')
def demo():
    return api_utils.response(200, fake_service.execute())