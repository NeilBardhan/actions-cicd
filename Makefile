src_dir := src/demo_py_pkg
test_dir := tests
python_src := $(shell find $(src_dir) -type f -name "*.py" || :)
python_src_pyc := $(shell find . -type f -name "*.pyc" || :)
test_src := $(shell find $(test_dir) -type f -name "*.py" || :)
pycache := $(shell find . -type d -name "__pycache__" || :)
pytest_cache := $(shell find . -type d -name "pytest_cache" || :)

.PHONY: install
install: ## Install this package and it's dependencies into the current environment
	pip install -e .
	pip install -r requirements.txt

.PHONY: test
test: ## Run unit tests
	pytest --cov=demo_py_pkg