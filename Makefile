.PHONY: help install install-dev test test-cov lint format type-check clean build

help:  ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install:  ## Install the package
	pip install -e .

install-dev:  ## Install the package with development dependencies
	pip install -e ".[dev]"

test:  ## Run tests
	pytest

test-cov:  ## Run tests with coverage
	pytest --cov=src/agentic_framework --cov-report=html --cov-report=term

test-unit:  ## Run only unit tests
	pytest -m unit

test-integration:  ## Run only integration tests
	pytest -m integration

lint:  ## Run linting
	flake8 src/ tests/ examples/

format:  ## Format code
	black src/ tests/ examples/
	isort src/ tests/ examples/

type-check:  ## Run type checking
	mypy src/

clean:  ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

build:  ## Build the package
	python -m build

check: lint type-check test  ## Run all checks (lint, type-check, test)

setup-venv:  ## Create and setup virtual environment
	python -m venv venv
	@echo "Virtual environment created. Activate with:"
	@echo "  source venv/bin/activate  (Linux/Mac)"
	@echo "  venv\\Scripts\\activate     (Windows)"