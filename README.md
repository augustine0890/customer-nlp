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
- Build container imaage and tag it `app_started`
  - `docker build -t app_started .`
- Run the container: `docker run app_started`