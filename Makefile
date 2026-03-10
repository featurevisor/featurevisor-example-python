PYTHON := .venv/bin/python
PIP := .venv/bin/pip

.PHONY: install build

install:
	python3 -m venv .venv
	$(PIP) install -r requirements.txt

build:
	$(PYTHON) main.py
