FROM ubuntu:23.04

ARG WAVE_VERSION
ARG PORT=10101

RUN apt update -y \
    && apt upgrade -y \
    && apt install -y \
    curl

RUN curl -L https://github.com/h2oai/wave/releases/download/v${WAVE_VERSION}/wave-${WAVE_VERSION}-linux-amd64.tar.gz -o wave-${WAVE_VERSION}-linux-amd64.tar.gz \
    && tar -xzf wave-${WAVE_VERSION}-linux-amd64.tar.gz \
    && mv wave-${WAVE_VERSION}-linux-amd64 /usr/wave

ENV H2O_WAVE_LISTEN=0.0.0.0:{PORT}
EXPOSE {PORT}
ENTRYPOINT /usr/wave/waved
