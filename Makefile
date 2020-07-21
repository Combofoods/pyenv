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
	python -m venv env && $(FOLDER)/pip install -r ./requirements.txt && $(FOLDER)/pip install -e . && $(FOLDER)/pip install --upgrade setuptools wheel twine pytest

build:
	@echo "Build the module"
	$(FOLDER)/python setup.py sdist bdist_wheel

publish_test:
	@echo "Sending the module to PIP"
	$(FOLDER)/python -m twine upload --config-file ~/.test.pypirc --repository testpypi dist/*

publish_prd:
	@echo "Sending the module to PIP"
	$(FOLDER)/python -m twine upload --config-file ~/.pypirc --repository pypi dist/*