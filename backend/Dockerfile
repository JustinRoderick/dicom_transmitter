FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy Dependencies and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Add the rest of the code
COPY . .

# Run backend on port 8000
EXPOSE 8000

# Run application.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]