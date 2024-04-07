src_dir := src/demo_py_pkg
test_dir := tests
python_src := $(shell find $(src_dir) -type f -name "*.py" || :)
python_src_pyc := $(shell find . -type f -name "*.pyc" || :)
test_src := $(shell find $(test_dir) -type f -name "*.py" || :)
pycache := $(shell find . -type d -name "__pycache__" || :)
pytest_cache := $(shell find . -type d -name "pytest_cache" || :)

.PHONY: venv
venv: ## Create and activate virtual environment
	/usr/bin/python3 -m pip install virtualenv
	/usr/bin/python3 -m virtualenv venv
	pwd && ls -al
	venv/bin/activate

.PHONY: install
install: ## Install this package and it's dependencies into the current environment
	pip install -e .
	pip install -r requirements.txt

.PHONY: test
test: ## Run unit tests
	pytest --cov=demo_py_pkg

.PHONY: build
build: ## Build python package
	python -m build --sdist
	python -m build --wheel