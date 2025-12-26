FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Create necessary directories
RUN mkdir -p logs outputs

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run as non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Default command
CMD ["python", "main.py", "--log-level", "INFO"]