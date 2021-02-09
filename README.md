# Code Runner as a Service

## Setup

- #### With docker

> 1. Follow the instructions [here](https://docs.docker.com/engine/install/) to install docker.
> 2. Then install docker compose by following [this](https://docs.docker.com/compose/install/).
> 3. Clone this respository and go to the root directory of this repo.
> 4. Create a network using `docker network create code_runner_net`.
> 5. Build the docker images using `docker-compose build`.
> 6. `cd` to the runner directory and again run `docker-compose build` to build the runner images.
> 7. Install docker-sync using `gem install docker-sync`. Make sure that the gem is in your `PATH`.
> 8. Inside the repos' root directory run `docker-sync-stack start`. If you get an error then stop the containers and restart using the same command.

- #### Without docker

> 1. Inside the repos' root directory create a new python environment using `python3 -m venv env` and activate it by running `source env/bin/activate`.
> 2. Install all the dependencies using `pip3 install -r code_runner/requirements/requirements.txt`. If you get an error in building psycopg2 then you must be missing necessary packages for building it.
> 3. Install rabbitmq by following this [link](https://www.rabbitmq.com/download.html).
> 4. Setup rabbitmq user by running `chmod +x shell_scripts/init_rabbitmq.sh && sh shell_scripts/init_rabbitmq.sh`.
> 4. Install postgreSQL and configure the database credentials. After that create a database named ***code_runner***.
> 5. Modify the .env.development.local and change all hosts to ***localhost*** and change the passwords.
> 6. Start the flask development server by running `python3 wsgi.py`.
> 7. Open another terminal and navigate to the repos' root and start celery worker by running `celery -A tasks worker --logLevel=DEBUG`.
> 8. You can now test it by visting `http://localhost:5000`.

## Demo

> I have created a public workspace on postman. You can test it from there and it can be used as a reference for API schema. [Here's the link](https://documenter.getpostman.com/view/4843397/TW76E5ZA#4a7b6c26-5672-4df5-9ffb-a1ef253160ec)
