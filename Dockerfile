FROM python:3.11.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY configs/ ./configs/
COPY data/sample/ ./data/sample/

CMD ["python", "src/benchmark.py"]
