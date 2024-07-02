FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install flask
RUN pip install requests

EXPOSE 5576

CMD ["python", "__main__.py"]
