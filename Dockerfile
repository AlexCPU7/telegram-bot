FROM python:3.7

ADD . /usr/src/app
WORKDIR /usr/src/app

RUN pip install -r requirements.txt
RUN python job_monitoring_bot/script_push_bot_.py