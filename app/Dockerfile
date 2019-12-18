FROM python:2.7.17-alpine3.10

ADD . /app

WORKDIR /app

RUN pip install -r /app/requirements.txt

CMD ["python /app/kinesis.py"]



