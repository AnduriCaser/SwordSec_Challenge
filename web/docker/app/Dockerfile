FROM python:3.8-slim


RUN mkdir /serve
WORKDIR /serve/app


COPY requirements.txt .
RUN pip install -r requirements.txt


COPY . .

ENTRYPOINT [ "python", "app.py" ]
