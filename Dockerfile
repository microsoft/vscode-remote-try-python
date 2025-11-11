# Base image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependency file first for better caching
COPY requirements.txt .

# Install dependencies (use no-cache to keep image light)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Expose port 5000 for Flask app
EXPOSE 5000

# Default command to run app.py
CMD ["python", "app.py"]
