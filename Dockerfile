# Use official Python runtime
FROM python:3.12-slim

WORKDIR /app

# Install system dependencies required by Chromium/Playwright
RUN apt-get update && apt-get install -y \
    wget curl gnupg ca-certificates fonts-liberation libnss3 libxss1 \
    libasound2 libatk1.0-0 libcups2 libxcomposite1 libxdamage1 \
    libxrandr2 libgbm1 libpango-1.0-0 libgtk-3-0 \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt and install Python packages
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Install Chromium browser for Playwright
RUN python -m playwright install chromium

# Copy the rest of your application code
COPY . .

# Optional: check browser version
RUN chromium-browser --version || true

# Run tests
CMD ["pytest", "-vsm", "normal"]



