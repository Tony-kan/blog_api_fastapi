# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip3 install -r requirements.txt

# Copy the app directory contents into /app
# COPY ./app /app
#COPY /app /app


# Expose the port that FastAPI will run on
EXPOSE 80

# Command to run FastAPI using uvicorn
CMD ["uvicorn", "app:app", "--host", "127.0.0.1", "--port", "8000", "--reload"]
