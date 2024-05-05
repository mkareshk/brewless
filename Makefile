install_dev:
	python -m pip install -U pip
	pip install -e .
	pip install -e .[dev]
	pre-commit install
	pre-commit autoupdate
	pre-commit run --all-files

run_local_llm:
	python -m brewless run_local_llm
generate:
	python -m brewless generate
