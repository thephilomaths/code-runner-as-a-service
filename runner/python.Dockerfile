FROM python:3.8
WORKDIR /code_runner
ADD shell_scripts/python_runner.sh runner.sh
RUN chmod +x runner.sh
