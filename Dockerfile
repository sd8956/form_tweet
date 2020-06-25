FROM python:3
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 3000
ENTRYPOINT gunicorn -b 0.0.0.0:3000 wsgi:app | celery -A task worker -B -l info
