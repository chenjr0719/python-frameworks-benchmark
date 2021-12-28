FROM python:3.7.2

ADD ./ /flask

WORKDIR flask

RUN pip3 install -r /flask/requirements.txt

WORKDIR /flask

EXPOSE 8080

ENV FLASK_APP=app.py

ENTRYPOINT ["/flask/conf/docker-entrypoint.sh"]

CMD gunicorn --bind 0.0.0.0:8080 --workers=2 app:app
