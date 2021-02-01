# !/bin/bash
# run this scrip after starting all the containers

docker-compose exec rabbit-mq rabbitmqctl add_user code_runner yeeyeeasshaircut
docker-compose exec rabbit-mq rabbitmqctl set_user_tags code_runner administrator
docker-compose exec rabbit-mq rabbitmqctl set_permissions -p / code_runner ".*" ".*" ".*"
