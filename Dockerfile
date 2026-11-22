# Line 1: Use official lightweight Python 3.11 slim base image
FROM python:3.11-slim

# Line 2: Prevent Python from writing .pyc files and enable unbuffered stdout logs
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

# Line 3: Set the working directory inside the container to /app
WORKDIR /app

# Line 4: Copy dependency manifest first to leverage Docker layer caching
COPY requirements.txt .

# Line 5: Install optional test runner without caching pip archives
RUN pip install --no-cache-dir -r requirements.txt

# Line 6: Copy application source code, datasets, tests, and main runner into /app
COPY src/ ./src/
COPY data/ ./data/
COPY tests/ ./tests/
COPY main.py .

# Line 7: Run the Arrival Time Estimator & 600-Bus Fleet Prototype on container start
CMD ["python", "main.py"]
