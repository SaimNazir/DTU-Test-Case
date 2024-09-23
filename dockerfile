# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the app.py file into the container at /app
COPY /home/saim/dtu_test_case/app/app.py /app/

# Copy any other necessary files (like requirements.txt if you have one)
# COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir Flask

# Make port available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV FLASK_APP=app.py

# Run app.py when the container launches
CMD ["python", "app.py"]