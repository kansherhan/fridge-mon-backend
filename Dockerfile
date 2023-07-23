FROM python:3.11.4

WORKDIR /fridge_mon

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "server.py"]
