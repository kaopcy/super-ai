# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application
COPY app/ app/

# Expose the Flask port
EXPOSE 5000

# Run the app
CMD ["python", "app/app.py"]