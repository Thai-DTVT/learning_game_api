FROM python:3.11

WORKDIR /

COPY ./requirements.txt /requirements.txt

RUN pip install --no-cache-dir --upgrade -r /requirements.txt

COPY ./game_api /game_api

CMD ["uvicorn", "--app-dir=.", "game_api.main:app", "--host", "0.0.0.0", "--port", "8080"]