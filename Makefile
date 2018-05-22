SHELL=bash
VIRTUALENV_DIR=.venv
ACTIVATE="$(VIRTUALENV_DIR)/bin/activate"

.PHONY: venv test lint clean

all: venv

venv:
	@echo "Creating python3 virtualenv in ${VIRTUALENV_DIR} dir"
	@tox -e py3-venv

dev-env:
	@echo "Creating python3 editable install in .venv"
	@tox -e py3-dev

lint:
	@echo "Linting with flake8..."
	@tox -e py3-lint

install:
	@echo "Installing gack to system..."
	@./setup.py install

dbgrun: dev-env
	@WERKZEUG_DEBUG_PIN=off $(VIRTUALENV_DIR)/bin/python gack/main.py --port=8080 --use_reloader=true

uninstall:
	@echo "Uninstalling gack from system..."
	@pip3 uninstall -y gack

clean:
	find . -name __pycache__ | xargs rm -rf
	find . -name "*.egg-info" | xargs rm -rf
	find . -name .tox | xargs rm -rf
	find . -name "*.pyc" | xargs rm -rf
