FROM python:3.7
MAINTAINER BHAVSINGH

COPY ./camino_form /camino_form
WORKDIR /camino_form

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:${PORT}"]