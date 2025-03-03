# Use the official Python image from the Docker Hub
FROM python:3.9-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirement.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirement.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port that the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app1.py"]