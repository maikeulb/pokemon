FROM python:3.6-alpine

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY pokemon.py config.py entrypoint.sh ./
ENV FLASK_APP pokemon.py
ENV FLASK_APP_CONFIG=config.DevelopmentConfig

EXPOSE 5000
RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
