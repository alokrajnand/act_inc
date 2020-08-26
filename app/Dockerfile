FROM python:3.8.3

ENV APP_ROOT /app
ENV CONFIG_ROOT /config


RUN mkdir ${CONFIG_ROOT}
COPY requirements.txt ${CONFIG_ROOT}/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r ${CONFIG_ROOT}/requirements.txt

RUN mkdir ${APP_ROOT}
WORKDIR ${APP_ROOT}

# static folder created
RUN mkdir -p ${APP_ROOT}/static/

ADD . ${APP_ROOT}
