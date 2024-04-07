src_dir := src/demo_py_pkg
test_dir := tests

.PHONY: test
test: ## Run unit tests
	pytest --cov=demo_py_pkg