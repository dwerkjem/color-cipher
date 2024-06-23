# Contributing to color-cipher

First and foremost, thank you for considering contributing to color-cipher. Your contributions help make this project better and more useful for everyone.

## Table of Contents

- [Contributing to color-cipher](#contributing-to-color-cipher)
  - [Table of Contents](#table-of-contents)
  - [How to Contribute](#how-to-contribute)
    - [Reporting Bugs](#reporting-bugs)
    - [Suggesting Enhancements](#suggesting-enhancements)
    - [Pull Requests](#pull-requests)
  - [Development Guidelines](#development-guidelines)
    - [Code Formatting](#code-formatting)
    - [Character Capitalization and Naming Conventions](#character-capitalization-and-naming-conventions)
    - [Commit Messages](#commit-messages)
  - [Getting Help](#getting-help)

## How to Contribute

### Reporting Bugs

If you encounter a bug, please create an issue on GitHub with the following details:

- **Summary:** A brief description of the issue.
- **Steps to Reproduce:** Clear steps to reproduce the bug.
- **Expected Results:** What you expected to happen.
- **Actual Results:** What happened?
- **Environment:** Information about your operating system, Python version, and any other relevant details.

### Suggesting Enhancements

To suggest a feature or enhancement, please open an issue on GitHub and provide:

- **Use Case:** Describe how this enhancement would be used.
- **Proposed Solution:** A detailed description of the suggested enhancement.
- **Alternatives Considered:** Any alternative solutions or features you've considered.

### Pull Requests

To submit a pull request (PR):

1. **Fork the Repository:** Create a fork of the project repository on GitHub.
2. **Create a Branch:** Create a new branch for your feature or bugfix (`git checkout -b feature/YourFeatureName`).
3. **Make Changes:** Implement your changes in the new branch.
4. **Run Tests:** Ensure all tests pass and add new tests for your changes if applicable.
5. **Commit Changes:** Commit your changes with a descriptive commit message.
6. **Push Changes:** Push your changes to your fork (`git push origin feature/YourFeatureName`).
7. **Open PR:** Open a pull request on the main repository with a detailed description of your changes.

## Development Guidelines

### Code Formatting

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code style. Use tools like `flake8` and `black` to ensure your code adheres to these guidelines.

- **Indentation:** Use 4 spaces per indentation level.
- **Imports:** Order imports in the following manner:
  1. Standard library imports
  2. Related third-party imports
  3. Local application/library-specific imports

Example:

```python
import os
import sys

import requests

from .my_module import my_function
```

### Character Capitalization and Naming Conventions

Consistent naming conventions and capitalization are crucial for readability and maintainability. Here are the guidelines:

- **Variables:** Use lowercase words separated by underscores.

  ```python
  max_length = 100
  user_name = "Derek"
  ```

- **Constants:** Use all uppercase letters with words separated by underscores.

  ```python
  MAX_RETRIES = 5
  API_KEY = "your_api_key_here"
  ```

- **Functions and Methods:** Use lowercase words separated by underscores.

  ```python
  def calculate_area(radius):
      pass

  def fetch_data(url):
      pass
  ```

- **Classes:** Use CamelCase for class names, starting each word with a capital letter.

  ```python
  class DataProcessor:
      pass

  class UserAccount:
      pass
  ```

- **Modules and Packages:** Use short, all-lowercase names. Underscores can be used if it improves readability.

  ```python
  import my_module
  from color_cipher import cipher_utils
  ```

- **Files:** Use lowercase words separated by underscores.

  ```plaintext
  my_script.py
  data_loader.py
  ```

### Commit Messages

Write clear and concise commit messages. Follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification:

- **feat:** A new feature
- **fix:** A bug fix
- **docs:** Documentation changes
- **style:** Code formatting changes (white space, formatting, missing semi-colons, etc)
- **refactor:** Code changes that neither fix a bug nor add a feature
- **test:** Adding missing tests or correcting existing tests
- **chore:** Changes to the build process or auxiliary tools and libraries such as documentation generation

Example:

```git commit
feat: add user authentication module

- Implemented user login and registration
- Added JWT-based authentication
```

## Getting Help

If you need help or have any questions, feel free to open an issue or reach out to the maintainers.

---

Thank you for your contributions! 🎉
