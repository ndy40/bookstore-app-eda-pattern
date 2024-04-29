FROM python:3.12-alpine
ENV PYTHONDONTWRITEBYTECODE=1

RUN python -m pip install --upgrade pip && pip install pipenv
COPY ./app/Pipfile ./app/Pipfile.lock ./
RUN pipenv install --dev --system --deploy

COPY ./app/ /code/
WORKDIR /code

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /code
USER appuser

