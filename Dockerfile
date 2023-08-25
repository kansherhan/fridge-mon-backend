FROM python:3.11.4

WORKDIR /fridge_mon

COPY . .

RUN pip install --upgrade pip==23.2.1
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 4978

CMD ["python", "server.py", "--debug"]
