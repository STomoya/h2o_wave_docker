FROM alpine:edge

ARG WAVE_VERSION=1.0.0
ARG PORT=10101

RUN apk add curl ca-certificates git gcompat

WORKDIR /opt/wave

RUN curl -sL \
      https://github.com/h2oai/wave/releases/download/v${WAVE_VERSION}/wave-${WAVE_VERSION}-linux-amd64.tar.gz \
      | tar -xzf- -C /opt/wave --strip-components=1 wave-${WAVE_VERSION}-linux-amd64

EXPOSE ${PORT}
EXPOSE 8000

ENV H2O_WAVE_LISTEN=0.0.0.0:${PORT}

ENTRYPOINT /opt/wave/waved
