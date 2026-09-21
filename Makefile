FILE_PATH ?=

.PHONY: web lab format lint check uv-def test-notebook run

web:
	uv run jupyter book start

lab:
	uv run jupyter lab

format:
	uv run ruff format .

lint:
	uv run ruff check . --fix
	uv run mypy .
	uv run nbqa mypy .

check:
	uv run pre-commit run --all-files

uv-def:
	uv sync --extra cuda --all-groups

test-notebook:
	@if [ -z "$(FILE_PATH)" ]; then echo "Error: FILE_PATH is required. Example: make test-notebook FILE_PATH=content/.../notebook.ipynb"; exit 1; fi
	@echo "Testing(CPU) the notebook: $(FILE_PATH)"
	uv sync --extra cpu
	uv run jupyter nbconvert --execute --to asciidoc $(FILE_PATH)
	@echo "Testing(GPU) the notebook: $(FILE_PATH)"
	uv sync --extra cuda
	uv run jupyter nbconvert --execute --to asciidoc $(FILE_PATH)
	@echo "Completed ✅️"
	$(MAKE) uv-def

run:
	@if [ -z "$(FILE_PATH)" ]; then echo "Error: FILE_PATH is required. Example: make run FILE_PATH=content/.../notebook.ipynb"; exit 1; fi
	@echo "Running: $(FILE_PATH)"
	uv run jupyter nbconvert --execute --to notebook --inplace $(FILE_PATH)
