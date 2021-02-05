FROM rabbitmq:3.8.11

ENV RABBITMQ_USER code_runner
ENV RABBITMQ_PASSWORD yeeyeeasshaircut
ENV RABBITMQ_PID_FILE /var/lib/rabbitmq/mnesia/rabbitmq

ADD shell_scripts/init_rabbitmq.sh /init.sh
RUN chmod +x /init.sh
EXPOSE 15672
EXPOSE 5672
EXPOSE 5671

CMD ["/init.sh"]
