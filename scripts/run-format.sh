#!/bin/bash

# Script to sort imports and format code using black for files in the src directory

echo "-> running ruff sort ..."
uv run ruff check --select I --fix exercise1/ exercise2/ exercise3/ tests/ # Check for isort issues and fix them

echo "-> running ruff format ..."
uv run ruff format exercise1/ exercise2/ exercise3/ tests/ # Format code using black

echo "-> running mypy ..."
uv run mypy exercise1/ exercise2/ exercise3/ tests/
