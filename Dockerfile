FROM python:3.12.6

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app /app
WORKDIR /app
RUN alembic upgrade head
RUN alembic revision --autogenerate -m "init"
RUN alembic upgrade head

CMD ["gunicorn", "main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]