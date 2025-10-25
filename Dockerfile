FROM python:3.12-slim

WORKDIR /app

# System dependencies for Playwright
RUN apt-get update && apt-get install -y \
    wget curl gnupg libnss3 libatk1.0-0 libatk-bridge2.0-0 libcups2 \
    libdrm2 libxkbcommon0 libxcomposite1 libxdamage1 libxfixes3 \
    libxrandr2 libgbm1 libasound2 libxshmfence1 \
    libpangocairo-1.0-0 libpango-1.0-0 libgtk-3-0 \
    fonts-liberation \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir playwright

# Copy project
COPY . .

# Install Playwright browsers
RUN python -m playwright install

ENV HEADLESS=true \
    PYTHONUNBUFFERED=1

CMD ["python", "-u", "-m", "pytest", "-v", "-s"]
