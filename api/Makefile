.DEFAULT: help
.PHONY: help bootstrap lint outdated clean

VENV = .venv
PYTHON = $(VENV)/bin/python3

help:
	@echo "Please use '$(MAKE) <target>' where <target> is one of the following:"
	@echo "  help        - show help information"
	@echo "  bootstrap   - initialize virtual environment and install dependencies"
	@echo "  lint        - inspect project source code for errors"
	@echo "  outdated    - list outdated project requirements"
	@echo "  clean       - clean up project environment"

bootstrap:
	python3 -m venv $(VENV)
	$(PYTHON) -m pip install pip==21.2.4 setuptools==57.4.0 wheel==0.37.0
	$(PYTHON) -m pip install -r requirements.txt
	$(PYTHON) -m pip install -r dev-requirements.txt
	$(PYTHON) -m pip install -r lsp-requirements.txt

lint: $(VENV)
	$(PYTHON) -m flake8 server.py

outdated: $(VENV)
	$(PYTHON) -m pip list --outdated --format=columns

clean:
	rm -rf .venv
