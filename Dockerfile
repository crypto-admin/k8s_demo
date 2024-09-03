FROM arm64v8/python:3.9-alpine

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirement.txt

CMD ["python", "app.py"]
