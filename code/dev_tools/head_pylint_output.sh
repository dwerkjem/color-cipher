#!/bin/bash

# Run pylint on all Python files, excluding the venv directory and __init__.py files
pylint_output=$(find . -type f -name "*.py" ! -name "__init__.py" ! -path "./venv/*" ! -path "./.venv/*" ! -path "./code/venv/*" -exec pylint {} +)

# Print the first 10 lines of pylint output
echo "$pylint_output" | head -n 10
