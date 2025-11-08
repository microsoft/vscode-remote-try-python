# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . /app

# Install dependencies (if any)
RUN pip install --no-cache-dir -r requirements.txt || true
RUN pip install pytest

# Default command: open bash
CMD ["/bin/bash"]

