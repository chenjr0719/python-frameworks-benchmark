FROM python:3.7.2

ADD ./ /sanic

WORKDIR sanic

RUN pip3 install -r /sanic/requirements.txt

WORKDIR /sanic

EXPOSE 8080

ENTRYPOINT ["/sanic/conf/docker-entrypoint.sh"]

CMD uvicorn app:app --host 0.0.0.0 --port 8080 --workers 2
 