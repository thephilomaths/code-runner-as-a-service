import os
import json
from .celery import app

@app.task
def run_code(data: str) -> str:
    data = json.loads(data)
    code: str = data['code']
    code_input: str = data['code_input']
    language: str = data['language']

    task_id = run_code.request.id

    path = 'runner/codes'
    code_filename = f'{str(task_id)}.{language}'
    input_filename = f'{str(task_id)}-input'

    with open(f'{path}/{code_filename}', 'w') as f:
        f.write(code)

    with open(f'{path}/{input_filename}', 'w') as f:
        f.write(code_input)

    cmd = f'python {path}/{code_filename}'
    run_cmd = f'cd runner && docker-compose run --rm python-runner {cmd}'
    sub_process = os.popen(run_cmd)

    output = sub_process.read()
    return output