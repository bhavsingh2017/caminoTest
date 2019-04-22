FROM python:3.7
MAINTAINER BHAVSINGH

USER root
ADD Camino_Form camino_form
WORKDIR camino_form

RUN ls -a
RUN pip install -r requirements.txt

CMD ["gunicorn", "Camino_Form.wsgi:application", "--log-file -", "0.0.0.0:$PORT"]