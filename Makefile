install_dev:
	python -m pip install -U pip
	pip install -e .
	pip install -e .[dev]
	pre-commit install
	pre-commit run --all-files
	pre-commit autoupdate

run_local_llm:
	python -m brewless run_local_llm
generate:
	python -m brewless generate
