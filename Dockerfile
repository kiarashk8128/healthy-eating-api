# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /code

# Install any necessary dependencies
RUN pip install --upgrade pip
COPY requirements.txt /code/

# Install the dependencies
RUN pip install -r requirements.txt


# Copy the current directory contents into the container at /code
COPY . /code/

# Add satic files to code for grappelli theme
RUN python manage.py collectstatic --noinput

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Run the application
CMD ["gunicorn", "health.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
