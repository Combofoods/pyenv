APP_NAME:=envpy
DOCKER_BASE_IMAGE_PYTHON:=python:3.8.3-alpine3.12
FOLDER:=env/bin/

venv:
	@echo "Open python venv"
	$(FOLDER)/pip install -r ./requirements.txt
	$(FOLDER)/pip install -e .

pytest: venv
	@echo "Running pytest ..."
	$(FOLDER)/pytest

# Setup

setup:
	@echo "Creating a development enviroment"
	python -m venv env && $(FOLDER)/pip install -r ./requirements.txt && $(FOLDER)/pip install -e . && $(FOLDER)/pip install --upgrade setuptools wheel twine
