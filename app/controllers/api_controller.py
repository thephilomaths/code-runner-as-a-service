from flask import Response
import json
from typing import Dict, Union


class ApiController:
    @staticmethod
    def response_data(data: Dict[str, any]) -> Response:
        response = {
            'data': data
        }

        return Response(response=response, status=200)

    @staticmethod
    def error_response(status_code: int, error_message: str) -> Response:
        response = {
            'error': error_message
        }
        return Response(response=json.dumps(response), status=status_code)

    @staticmethod
    def request_data(body: Union[str, bytes]) -> Dict[str, any]:
        body = json.loads(body)
        return body
