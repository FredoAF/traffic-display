FROM python:alpine

RUN pip install flask tinydb pytz
COPY ./app/ /app
ENTRYPOINT ["/usr/local/bin/python", "/app/main.py"]
