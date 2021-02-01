from typing import Union
from app.controllers.api_controller import ApiController


class RunController(ApiController):
    def run(self, body: Union[str, bytes]):
        body = self.request_data(body=body)
        data = body.get('data')
        if data is None:
            return self.error_response(status_code=422, error_message='Unprocessable entity')

        language = data.get('language')
        code = data.get('code')
        test_case = data.get('test_case')

        if language is None or code is None or test_case is None:
            return self.error_response(status_code=422, error_message='Unprocessable entity')

        # TODO: Call the celery worker
