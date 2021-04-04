FROM python:3.8
WORKDIR /code_runner
COPY code_runner/requirements/requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
RUN chmod +x shell_scripts/gunicorn_starter.sh
RUN chmod +x runner/shell_scripts/cpp_runner.sh
RUN chmod +x runner/shell_scripts/python_runner.sh
RUN chmod +x runner/shell_scripts/java_runner.sh