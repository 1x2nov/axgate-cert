FROM namhoonkooo/snort-automation

ENTRYPOINT su - gitrun
WORKDIR /snort
RUN ls -al
