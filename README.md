- A simple web app for classifying and summarizing customer feedback.

## Development Environments
- Create a virtual environment
  - `python3 -m venv fastapi`
- Activate and Deactivate virtual environment
  - `source fastapi/bin/activate`
  - `deactivate` run in the prompt to deactivate the virtual environment

## Package Management
- List of packages installed: `python3 -m pip list`
- Install the `FastAPI` package: `pip install fastapi`
- Collate current packages installed in a project into a file
  - `pip freeze > requrements.txt`
- Install packages from `requirements.txt`
  - `pip install -r requirements.txt`

## Setting a Docker
- Build container imaage and tag it `fastapi-nlp`
  - `docker build -t fastapi-nlp .`
- Run the container: `docker run -d --name customer-nlp-application -p 8000:8000 fastapi-nlp`

## FastAPI Application
- Start application using `uvicorn`
  - `uvicorn app:app --port 8000 --reload`
    - `file:instance`: the file containing the instance of FastAPI and the name variable holding the FastAPI instance.
    - `--port`: PORT the application will be served on.
    - `--reload`: an optional argument included to restart the application on every file change.