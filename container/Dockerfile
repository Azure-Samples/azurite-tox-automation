
# [Choice] Python version: 3, 3.9, 3.8, 3.7, 3.6
ARG VARIANT="3.9"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

ADD . .

ADD ./container/service_start.sh .
RUN chmod +x service_start.sh

RUN pip install azure-storage-blob --upgrade
RUN pip install -r requirements.txt

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y nodejs \
    npm

# # Install npm itself to install npm packages
# RUN apt-get update && apt-get upgrade -y && \
#     apt-get install -y python-pytest

RUN npm install -g azurite

ENV PATH="/usr/bin/pytest:${PATH}"
ENV PATH="/usr/local/bin/python3.9:${PATH}"