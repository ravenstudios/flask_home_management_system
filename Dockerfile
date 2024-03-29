# Use the official Python image as base
FROM python:3.10

# Set environment variables
ENV FLASK_APP=app
ENV FLASK_RUN_PORT=5000
ENV FLASK_RUN_HOST=0.0.0.0
# Set working directory in the container
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 to the outside world
EXPOSE 5000

# Command to run the application
CMD ["flask", "run"]
