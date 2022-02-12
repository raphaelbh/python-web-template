FROM python:3.9.10-alpine

COPY ./app /app
WORKDIR /app

RUN pip install -r requirements.txt

RUN adduser -D appuser
USER appuser
		
CMD gunicorn --bind 0.0.0.0:$PORT wsgi