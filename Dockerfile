# Use Python 3.10 as base image
FROM python:3.10-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in docker_requirements.txt
RUN pip install --no-cache-dir -r docker_requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Run the app.
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
