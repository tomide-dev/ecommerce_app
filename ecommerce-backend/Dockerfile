# Use Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run app
CMD ["sh", "-c", "sleep 5 && gunicorn -b 0.0.0.0:5000 app:app"]
