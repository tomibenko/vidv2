FROM  python:3.9-alpha
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /app
COPY . /app
EXPOSE 8080
CMD ["python", "app.py"]