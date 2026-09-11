.PHONY: web lab format lint check

web:
	uv run jupyter book start

lab:
	uv run jupyter lab

format:
	uv run ruff format .

lint:
	uv run ruff check . --fix
	uv run mypy .

check:
	uv run pre-commit run --all-files
