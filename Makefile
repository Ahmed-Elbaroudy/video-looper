# Python environment
PYTHON ?= python

# Project settings
PROJECT_NAME = video_looper

.PHONY: install test lint format check clean

install:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

install-dev:
	pip install -r requirements-dev.txt

test:
	pytest tests/ --cov=$(PROJECT_NAME) --cov-report=term-missing

lint:
	flake8 $(PROJECT_NAME) tests
	mypy $(PROJECT_NAME) tests

format:
	black $(PROJECT_NAME) tests
	isort $(PROJECT_NAME) tests

check:
	make lint
	make test

clean:
	rm -rf __pycache__
	rm -rf *.py[cod]
	rm -rf *.so
	rm -rf .Python
	rm -rf build/
	rm -rf develop-eggs/
	rm -rf dist/
	rm -rf downloads/
	rm -rf eggs/
	rm -rf .eggs/
	rm -rf lib/
	rm -rf lib64/
	rm -rf parts/
	rm -rf sdist/
	rm -rf var/
	rm -rf wheels/
	rm -rf *.egg-info/
	rm -rf .installed.cfg
	rm -rf *.egg
