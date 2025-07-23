# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy only the dependency file first
COPY requirements.txt .

# Install dependencies first — cached unless requirements.txt changes
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of your application
COPY . .

# Expose Flask port
EXPOSE 5000

# Start Flask app
CMD ["python", "app.py"]
