FROM python:3.9-buster

WORKDIR /opt/app

RUN apt-get -y update && apt-get -y upgrade

COPY pyproject.toml poetry.lock ./
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false


RUN poetry install --no-root

# Expose the port used by the Django development server
EXPOSE 8000

COPY . /opt/app/

# Set the command to run the Django development server
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]