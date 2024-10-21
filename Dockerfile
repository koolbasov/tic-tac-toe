FROM python:3.11.10-alpine3.20

WORKDIR /app/

COPY . /app/

CMD ["python", "app.py"]