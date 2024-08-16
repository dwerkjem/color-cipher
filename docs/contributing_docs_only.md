# Contributing to color-cipher Documentation

Welcome to the color-cipher documentation project! We are excited to have you here. This document provides guidelines for contributing to the color-cipher documentation.

## Table of Contents

- [Contributing to color-cipher Documentation](#contributing-to-color-cipher-documentation)
  - [Table of Contents](#table-of-contents)
  - [How to Contribute](#how-to-contribute)

## How to Contribute

Color-cipher documentation is kept in the `docs` directory of the project repository and the main [README](../README.md). To contribute to the documentation, follow these steps:

Notes:
The documentation is written in Markdown format. If you are not familiar with Markdown, you can refer to the [Markdown Guide](https://www.markdownguide.org/).

approved contributors can make changes directly to the `docs` directory. If you are not an approved contributor, you can fork the repository, make changes, and submit a pull request. see [Contributing to color-cipher](../contributing.md) for more information.

---

steps for contributing to the documentation:

1. **get the repository:** if you are an approved contributor, clone the repository to your local machine. If you are not an approved contributor, fork the repository and clone the fork to your local machine.
    - to clone the repository if you are an approved contributor: in vs code, open the command palette (Ctrl+Shift+P) and run the `git clone https://github.com/dwerkjem/color-cipher` command. or open the Explorer, click the `Clone Repository` button, and paste the repository URL `https://github.com/dwerkjem/color-cipher.git`.
    - to fork the repository if you are not an approved contributor:
        1. go to the color-cipher repository on GitHub: [dwerkjem/color-cipher](https://github.com/dwerkjem/color-cipher).
        2. click the `Fork` button in the upper right corner of the page.
        3. clone the fork to your local machine:
            - in vscode, open the command palette (Ctrl+Shift+P) and run the `git clone` command with the URL of your forked repository.
            - or open the Explorer, click the `Clone Repository` button, and paste the URL of your forked repository.
2. **make changes:** make changes to the documentation files in the `docs` directory and the main [README](../README.md) file as needed. Note that any sub-directories in the `docs` directory are also part of the documentation.\
3. **preview changes:** to preview the changes locally, you can use the `Markdown All in One` extension in vscode. Open the Markdown file you want to preview, right-click in the editor, and select `Open Preview` or push `(Ctrl+k v)`. This will open a side-by-side preview of the Markdown file. You can also use the `Markdown Preview Enhanced` extension for more advanced features.
4. **commit changes:** once you are satisfied with the changes, commit them to your local repository. In vscode, open the Source Control view, stage the changes, enter a commit message, and click the checkmark icon to commit the changes.
    - use descriptive commit messages that explain the purpose of the changes.
    - if you are an approved contributor, you can commit changes directly to the main repository.
5. **push changes:** push the changes to your forked repository on GitHub. In vscode, open the Source Control view, click the ellipsis icon (`...`), and select `Push`. you may need to sign in to GitHub if you haven't already.
   - if you are an approved contributor, you can push changes directly to the main repository.
   - you may need to run `git push --set-upstream origin main` to set the upstream branch.
   - if you get a message about user.email and user.name, you can set these values in vscode by running the `git config --global user.email "(your email)"` and `git config --global user.name "(your name)"` commands.
   - if you are not an approved contributor, you will need to open a pull request to submit your changes.
   - if you are an approved contributor, you can open a pull request to submit your changes, but you can also push changes directly to the main repository.
6. **open a pull request (if needed):** if you are not an approved contributor, open a pull request to submit your changes. Go to your forked repository on GitHub, click the `New pull request` button, select the main repository as the base, and compare the changes. Enter a title and description for the pull request, and click the `Create pull request` button.
7. **review and merge changes:** an approved contributor will review the changes and merge them into the main repository if they are approved.
8. **update local repository:** if your changes are merged, you can update your local repository by pulling the changes from the main repository. In vscode, open the Source Control view, click the ellipsis icon (`...`), and select `Pull`.

---

Thank you for contributing to the color-cipher documentation! If you have any questions or need help, feel free to reach out to the project maintainers or other contributors. We appreciate your help in making the documentation better for everyone.