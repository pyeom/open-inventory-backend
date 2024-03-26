FROM python:3.12-slim
ENV PYTHONBUFFERED=1
RUN apt-get update && apt-get -y install libpq-dev gcc
WORKDIR /app
COPY ./requirements.txt /app
RUN pip3 install --no-cache-dir --disable-pip-version-check -r requirements.txt
COPY . /app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
