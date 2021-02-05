FROM gcc:latest
WORKDIR /code_runner
ADD shell_scripts/cpp_runner.sh shell_scripts/cpp_runner.sh
RUN chmod +x shell_scripts/cpp_runner.sh
