FROM python:3.11-slim

WORKDIR /app

# Copy requirements first, then install
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Then copy the rest of the app
COPY . .

EXPOSE 5000
CMD ["python", "app.py"]
