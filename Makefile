FILE_PATH ?=

.PHONY: web lab format lint check uv-def test-notebook

web:
	uv run jupyter book start

lab:
	uv run jupyter lab

format:
	uv run ruff format .

lint:
	uv run ruff check . --fix
	uv run nbqa mypy .

check:
	uv run pre-commit run --all-files

uv-def:
	uv sync --extra cuda --all-groups

test-notebook:
	@echo "Testing(CPU) the notebook: $(FILE_PATH)"
	uv sync --extra cpu
	uv run jupyter nbconvert --execute --to asciidoc $(FILE_PATH)
	@echo "Testing(GPU) the notebook: $(FILE_PATH)"
	uv sync --extra cuda
	uv run jupyter nbconvert --execute --to asciidoc $(FILE_PATH)
	@echo "Completed ✅️"
	make uv-def

run:
	@echo "Running: $(FILE_PATH)"
	uv run jupyter nbconvert --execute --to notebook --inplace $(FILE_PATH)
