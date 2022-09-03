FROM python:3.8-slim


RUN mkdir /serve
WORKDIR /serve/consume


COPY requirements.txt .
RUN pip install -r requirements.txt


COPY . .

ENTRYPOINT [ "python", "consume.py" ]
