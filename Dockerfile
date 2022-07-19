FROM python:3.10-slim-buster

RUN mkdir /code
WORKDIR /code
ADD . /code

RUN pip install poetry && poetry install && poetry run python manage.py collectstatic --noinput

CMD [ "poetry", "run", "gunicorn", "-w", "10", "-b", "0.0.0.0:8000", "config.wsgi" ]
