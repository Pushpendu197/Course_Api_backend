# Use the official Python 3 image as the base image
FROM python:3

# Set environment variable to ensure Python output is not buffered
ENV PYTHONUNBUFFERED 1

RUN mkdir /back_end

# Set the working directory in the container
WORKDIR /back_end

# Copy the current directory contents into the container at /back_end
COPY . /back_end/

# Install the required packages from requirements.txt
RUN pip install -r requirements.txt