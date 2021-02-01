FROM python:3.8
WORKDIR /code_runner
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
