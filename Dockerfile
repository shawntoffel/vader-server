FROM python:3.8.0-alpine3.10
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "server.py"]