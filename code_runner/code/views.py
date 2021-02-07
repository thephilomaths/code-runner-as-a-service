import json

from celery.result import AsyncResult
from celery.exceptions import TimeLimitExceeded, TimeoutError
from flask import Blueprint, request
from flask.views import MethodView

from tasks import tasks
from ..utils import api
from tasks import celery

blueprint = Blueprint('__code__', __name__)


class Code(MethodView):
    worker_args = {}

    def request_data(self):
        """Returns the request data"""

        body = api.request_data(request.get_data())
        data = body.get('data')

        if data is None:
            return api.error_response(status_code=422, error_message='Unprocessable Entity')

        language = data.get('language')
        code = data.get('code')
        code_input = data.get('code_input')
        time_limit = data.get('time_limit') or 1

        if language is None or code is None or code_input is None or language not in ['cpp', 'py', 'java'] \
                or type(time_limit) is not int or time_limit <= 0:
            return api.error_response(status_code=422, error_message='Unprocessable Entity')

        self.worker_args = {
            'language': language,
            'code': code,
            'code_input': code_input,
            'time_limit': time_limit
        }


class RunCode(Code):
    def post(self):
        """Synchronously run code and return the output"""
        self.request_data()

        response = {}

        try:
            result: str = tasks.run_code \
                .apply_async(args=[json.dumps(self.worker_args)], ignore_result=False) \
                .get(timeout=120)
            if result.startswith('Error:'):
                response['error'] = result
            else:
                response['result'] = result
            return api.response_data(data=response)
        except (TimeLimitExceeded, TimeoutError):
            return api.error_response(status_code=500, error_message='Task Timed Out')


class RunCodeAsync(Code):
    def post(self):
        """Asynchronously run code and return the task_id"""
        self.request_data()

        try:
            result = tasks.run_code.apply_async(args=[json.dumps(self.worker_args)], ignore_result=False)
            response = {
                'data': {
                    'task_id': result.task_id
                }
            }
            return api.response_data(data=response)
        except (TimeLimitExceeded, TimeoutError):
            return api.error_response(status_code=500, error_message='Task Timed Out')

    def get(self, task_id):
        """Returns the task result of the corresponding task id"""

        result = AsyncResult(id=task_id, app=celery.app)

        response = {}
        if not result.ready():
            response['data'] = {
                'result': 'Task is pending.'
            }
            return api.response_data(data=response)

        response['data'] = {
            'result': result.result
        }

        return api.response_data(data=response)


@blueprint.route('/', methods=['GET'])
def root_route():
    return "Get rid of that ol' yee yee ass haircut"
