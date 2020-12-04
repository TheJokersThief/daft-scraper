.PHONY: test coverage lint docs clean dev install help export_conf

override FLASKS_RUN_FLAGS+=-p 5001

help: ## Show help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

ensure-poetry:
	@if ! [ -x $(command -v poetry) ]; then \
		echo "Please install poetry (e.g. pip install poetry)"; \
		exit 1; \
	fi

lint: ensure-poetry  ## Lint files for common errors and styling fixes
	poetry check
	poetry run flake8 --ignore F821,W504 daft_scraper tests

test: ensure-poetry lint  ## Run unit tests
	poetry run pytest tests --cov=daft_scraper --strict tests

coverage: ensure-poetry test  ## Output coverage stats
	poetry run coverage report -m
	poetry run coverage html
	@echo "coverage report: file://`pwd`/htmlcov/index.html"

clean:
	find . -name '*.pyc' -delete
	find . -name __pycache__ -delete
	rm -rf .coverage dist build htmlcov *.egg-info

dev: ensure-poetry clean  ## Install project and dev dependencies
	poetry install

install: ensure-poetry clean  ## Install project without dev dependencies
	poetry install --no-dev

export_conf:  ## Export the poetry lockfile to requirements.txt
	poetry export -f requirements.txt --output requirements.txt --without-hashes

publish:
	poetry build
	poetry publish
