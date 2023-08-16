FROM python:3.11.4-alpine

WORKDIR /fridge_mon

COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "server.py", "--debug"]
