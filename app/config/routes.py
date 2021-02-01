from flask import Blueprint, Response
from ..controllers import RunController, OutputController

routes = Blueprint('route', __name__)


@routes.route('/run', methods=['POST'])
def run_handler():
    return Response(response='Hello from run', status=200)


@routes.route('/get-output', methods=['GET'])
def output_handler():
    return Response(response='Hello from get-output', status=200)
