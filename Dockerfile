FROM python:3.12-alpine
ENV PYTHONDONTWRITEBYTECODE=1

COPY ./bookstore/Pipfile ./bookstore/Pipfile.lock ./
RUN python -m pip install --upgrade pip && pip install pipenv
RUN pipenv install --dev --system --deploy

COPY . /code
WORKDIR /code/bookstore

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /code
USER appuser

CMD ["python", "cli.py"]
