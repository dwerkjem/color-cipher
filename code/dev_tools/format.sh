#!/bin/bash

# Paths are relative to the root of the git repository

# Run pylint on all Python files, excluding the venv directory
find . -type f -name "*.py" ! -path "./venv/*" ! -path "./.venv/*" ! -path "./code/venv/*" -exec pylint {} +

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
