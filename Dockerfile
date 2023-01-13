FROM python:3.10-slim

# Set working directory to /usr/src/app
WORKDIR /usr/src/app
# Copy the file with the requirements to the /app directory.
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy the contents of the current local directory to the container's working directory
ADD . /usr/src/app/
# Run a command
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
# CMD ["python", "app.py"]