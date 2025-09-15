FROM ubuntu:latest
LABEL authors="Hello's"

ENTRYPOINT ["top", "-b"]