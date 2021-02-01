# !/bin/bash
# run this scrip after starting all the containers

docker-compose exec rabbitmqctl add_user code_runner yeeyeeasshaircut &&
docker-compose exec rabbitmqctl set_user_tags code_runner administrator &&
docker-compose exec rabbitmqctl set_permissions -p / code_runner ".*" ".*" ".*""
