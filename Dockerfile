# Using a minimal and secure Python image
FROM python:3.11-slim

# Setting environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Setting working directory
WORKDIR /

# Installing dependencies securely
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copying only necessary files
COPY app.py .

# Exposing correspondent port
EXPOSE 5000

# Running with Gunicorn in production mode
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
