from flask import Blueprint, Response, request
from app.controllers.run_controller import RunController

routes = Blueprint('route', __name__)


@routes.route('/run', methods=['POST'])
def run_handler():
    body = request.get_data()
    response = RunController().run(body=body)
    return response


@routes.route('/get-output', methods=['GET'])
def output_handler():
    return Response(response='Hello from get-output', status=200)
