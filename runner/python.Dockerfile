FROM python:3.8
WORKDIR /code_runner
ADD shell_scripts/python_runner.sh shell_scripts/python_runner.sh
RUN chmod +x shell_scripts/python_runner.sh
