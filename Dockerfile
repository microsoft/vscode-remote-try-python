# Start from a lightweight Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy dependency file if exists
COPY requirements.txt .

# Install dependencies (if no requirements.txt, this will just skip)
RUN pip install --no-cache-dir -r requirements.txt || true

# Copy all project files into container
COPY . .

# Expose port 8000 for development servers
EXPOSE 8000

# Default command (you can change this if you use another file)
CMD ["python", "app.py"]
