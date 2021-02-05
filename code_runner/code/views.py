import json

from celery.exceptions import TimeLimitExceeded, TimeoutError
from flask import Blueprint, request

from ..utils import api
from tasks import tasks

blueprint = Blueprint('__code__', __name__)


@blueprint.route('/run', methods=['POST'])
def run():
    body = api.request_data(request.get_data())
    data = body.get('data')

    if data is None:
        return api.error_response(status_code=422, error_message='Unprocessable entity')

    language = data.get('language')
    code = data.get('code')
    code_input = data.get('code_input')
    time_limit = data.get('time_limit') or 1

    if language is None or code is None or code_input is None or language not in ['cpp', 'py', 'java'] \
            or type(time_limit) is not int:
        return api.error_response(status_code=422, error_message='Unprocessable entity')

    worker_args = {
        'language': language,
        'code': code,
        'code_input': code_input,
        'time_limit': time_limit
    }

    response = {}

    try:
        result: str = tasks.run_code \
            .apply_async(args=[json.dumps(worker_args)], ignore_result=False) \
            .get(timeout=120)
        if result.startswith('Error:'):
            response['error'] = result
        else:
            response['result'] = result
        return api.response_data(data=response)
    except (TimeLimitExceeded, TimeoutError):
        return api.error_response(status_code=500, error_message='Task Timed Out')
