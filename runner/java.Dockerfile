FROM openjdk:latest
WORKDIR /code_runner
ADD shell_scripts/java_runner.sh shell_scripts/java_runner.sh
RUN chmod +x shell_scripts/java_runner.sh
