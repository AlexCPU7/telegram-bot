FROM python:3.7

ENV PYTHONUNBUFFERED 1

COPY /job_monitoring_bot /usr/src/app
COPY requirements.txt /usr/src/app

WORKDIR /usr/src/app

RUN pip install -r requirements.txt
#RUN python job_monitoring_bot/script_push_bot.py