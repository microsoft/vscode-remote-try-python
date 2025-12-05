# Use the same base image as devcontainer.json
FROM mcr.microsoft.com/devcontainers/python:1-3.12

# Set working directory inside the container
WORKDIR /app

# Copy dependency list and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Expose the port used by the app
EXPOSE 9000

# Run the sample app
CMD ["python", "app.py"]
