FROM python:3.8-slim


RUN mkdir /service
WORKDIR /service/send


COPY requirements.txt .
RUN pip install -r requirements.txt


COPY . .

ENTRYPOINT [ "python", "send.py" ]
