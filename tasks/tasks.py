import os
import json
from datetime import datetime

from .celery import app
from code_runner import code
from code_runner import app as flask_app


@app.task
def run_code(data):
    data = json.loads(data)
    code_ = data['code']
    code_input = data['code_input']
    language = data['language']
    time_limit = int(data['time_limit'])

    task_id: str = run_code.request.id

    code_path = 'runner/codes'
    shell_script_path = 'runner/shell_scripts'
    code_filename = f'{str(task_id)}.{language}'
    input_filename = f'{str(task_id)}-input'

    with open(f'{code_path}/{code_filename}', 'w') as f:
        f.write(code_)

    with open(f'{code_path}/{input_filename}', 'w') as f:
        f.write(code_input)

    run_cmd = ''
    execution_log = code.models.ExecutionLog()
    execution_log.created_at = datetime.now()

    print(data)
    print(os.getcwd())
    print(f'{code_path}/{code_filename}')

    if language == 'py':
        execution_log.language = code.models.Language.python
        """For python time limit taken is 5 times relative to that of cpp.
        This assumption is based on https://www.hackerrank.com/environment"""
        cmd = f'{shell_script_path}/python_runner.sh ' \
              f'"{time_limit * 5}s" ' \
              f'"python" ' \
              f'"{code_path}/{code_filename}" ' \
              f'"{code_path}/{input_filename}"'
        run_cmd = f'cd runner && docker-compose run --rm python-runner {cmd}'
    elif language == 'cpp':
        execution_log.language = code.models.Language.cpp
        cmd = f'{shell_script_path}/cpp_runner.sh ' \
              f'"{time_limit}s" ' \
              f'"g++" ' \
              f'"{input_filename}_output" ' \
              f'"{code_path}/{code_filename}" ' \
              f'"{code_path}/{input_filename}"'
        run_cmd = f'cd runner && docker-compose run --rm cpp-runner {cmd}'
    elif language == 'java':
        execution_log.language = code.models.Language.java
        output_filename = input_filename.split('.')[0]
        cmd = f'{shell_script_path}/java_runner.sh ' \
              f'"{time_limit * 2}s" ' \
              f'"javac" '  \
              f'"{code_path}/{code_filename}" '\
              f'"{code_path}/{input_filename}" '
        run_cmd = f'cd runner && docker-compose run --rm java-runner {cmd}'          

    task_start_time = datetime.now()
    sub_process = os.popen(run_cmd)
    output: str = sub_process.read()
    os.system(f'rm {code_path}/{input_filename} {code_path}/{code_filename}')
    task_end_time = datetime.now()

    execution_log.execution_time = (task_end_time - task_start_time).seconds

    if output.startswith('Error'):
        execution_log.error_reason = code.models.ErrorReason.syntax_or_runtime
        execution_log.state = code.models.ExecutionState.error
    elif output.startswith('Time Limit Exceeded'):
        execution_log.error_reason = code.models.ErrorReason.tle
        execution_log.state = code.models.ExecutionState.error
    else:
        execution_log.error_reason = code.models.ErrorReason.no_error
        execution_log.state = code.models.ExecutionState.success

    with flask_app.app_context():
        execution_log.create()

    return output
