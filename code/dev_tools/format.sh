#!/bin/bash

# Paths are relative to the root of the git repository

# Run pylint on all Python files, excluding the venv directory and __init__.py files
pylint_output=$(find . -type f -name "*.py" ! -name "__init__.py" ! -path "./venv/*" ! -path "./.venv/*" ! -path "./code/venv/*" -exec pylint {} +)
pylint_score=$(echo "$pylint_output" | grep "Your code has been rated at" | awk '{print $7}' | cut -d'/' -f1)

# Check pylint score
if (( $(echo "$pylint_score < 9.0" | bc -l) )); then
  echo "Pylint score is below 9.0: $pylint_score"
  echo "$pylint_output"
  exit 1
else
  echo "Pylint score is 9.0 or above: $pylint_score"
  echo "$pylint_output"
fi

# Format Python files using black
black .

# Get list of files that have been added, copied, modified, or renamed
FILES=$(git diff --cached --name-only --diff-filter=ACMR | sed 's| |\\ |g')
[ -z "$FILES" ] && exit 0

# Prettify all selected files
echo "$FILES" | xargs ./node_modules/.bin/prettier --ignore-unknown --write

# Add back the modified/prettified files to staging
echo "$FILES" | xargs git add

exit 0
