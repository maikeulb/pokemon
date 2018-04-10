FROM python:3.6-alpine

COPY requirements.txt requirements.txt

RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY pokemon.py config.py entrypoint.sh ./

RUN chmod +x ./entrypoint.sh

ENV FLASK_APP pokemon.py
ENV FLASK_APP_CONFIG=config.ProductionConfig

EXPOSE 5000
ENTRYPOINT ["./entrypoint.sh"]
