FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/
COPY tests/ tests/

ENV OPENROUTER_API_KEY=your_api_key_here

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
