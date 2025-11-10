# Start from official Python slim image
FROM python:3.11-slim

# Set container working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 9000

# Run app
CMD ["flask", "run", "--host=0.0.0.0", "--port=9000"]
