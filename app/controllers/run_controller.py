import json
from typing import Union
from app.controllers.api_controller import ApiController
from app.workers import tasks
from celery.exceptions import TimeLimitExceeded


class RunController(ApiController):
    def run(self, body: Union[str, bytes]):
        body = self.request_data(body=body)
        data = body.get('data')
        if data is None:
            return self.error_response(status_code=422, error_message='Unprocessable entity')

        language = data.get('language')
        code = data.get('code')
        code_input = data.get('code_input')
        time_limit = data.get('time_limit') or 1

        if language is None or code is None or code_input is None:
            return self.error_response(status_code=422, error_message='Unprocessable entity')

        worker_args = {
            'language': language,
            'code': code,
            'code_input': code_input,
            'time_limit': time_limit
        }

        try:
            result = tasks.run_code.apply_async(args=[json.dumps(worker_args)])
            res_data = {
                'result': result.get()
            }
            return self.response_data(data=res_data)
        except TimeLimitExceeded:
            return 'Time Limit Exceeded'
