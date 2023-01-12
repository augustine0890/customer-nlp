FROM python:3.10-alpine

# Set working directory to /usr/src/app
WORKDIR /usr/src/app
# Copy the contents of the current local directory to the container's working directory
ADD . /usr/src/app/
# Run a command
CMD ["python", "app.py"]