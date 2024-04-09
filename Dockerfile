FROM  python:3.9-alpine
WORKDIR /app
COPY . /app
EXPOSE 8080
CMD ["python", "app.py"]
