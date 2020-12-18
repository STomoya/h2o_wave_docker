FROM ubuntu:18.04

ARG VERSION=0.10.0

RUN apt update -y \
    && apt upgrade -y \
    && apt install -y \
    curl

RUN curl -L https://github.com/h2oai/wave/releases/download/v${VERSION}/wave-${VERSION}-linux-amd64.tar.gz -o wave-${VERSION}-linux-amd64.tar.gz \
    && tar -xzf wave-${VERSION}-linux-amd64.tar.gz \
    && mv wave-${VERSION}-linux-amd64 /usr/wave