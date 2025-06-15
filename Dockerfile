# Use an official Python image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn qrcode[pil]

# Expose the port FastAPI runs on
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "qr_api:app", "--host", "0.0.0.0", "--port", "8000"]
