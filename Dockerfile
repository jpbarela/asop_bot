FROM python:3.11-slim

WORKDIR /app

RUN pip3 install poetry
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock /app/

RUN poetry install --with asop_bot --no-root

COPY ./asop_bot /app/

CMD ["streamlit", "run", "/app/asop_bot.py"]
