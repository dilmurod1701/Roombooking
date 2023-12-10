FROM python:3.11-alpine

ENV PYTHONBUFFERED=1
ENV PYTHONUNBUFFERED=1
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
WORKDIR /app
COPY . /app
EXPOSE 8000

CMD ["python", "manage.py", "runserver"]
