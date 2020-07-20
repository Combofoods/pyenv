FROM python:3.8.3-alpine3.12

ARG APP_NAME=envpy
ARG DEFAULT_USER=python

# Default System configs
RUN apk add --no-cache gcc \
    && addgroup --gid 1000 -S ${DEFAULT_USER} \
    && adduser --uid 1000 -D -G ${DEFAULT_USER} -g "${DEFAULT_USER}" ${DEFAULT_USER} ${DEFAULT_USER} \
    && ln -sT /usr/local/bin/python /bin/python3 \
    && chmod +x /bin/python3

# APP Install Requirements

COPY . /tmp/${APP_NAME}

WORKDIR /tmp/${APP_NAME}

RUN pip install -r requirements.txt \
    && pip install -e .

# App Configurations

USER 1000:1000
ENTRYPOINT [ "pytest" ]