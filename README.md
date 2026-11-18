# Student Task Manager

A simple Python console application that helps students organize and manage their academic tasks. This project demonstrates Python programming, Git version control, GitHub collaboration, and automated testing.

## Features

- Add new tasks.
- Display all tasks.
- Mark pending tasks as completed.
- Delete existing tasks.
- Validate empty task titles.
- Remove unnecessary spaces from task titles.
- Maintain unique task IDs after deletion.
- Automated unit testing using GitHub Actions.

## Technologies Used

- Python 3
- Git
- GitHub
- Python unittest
- GitHub Actions

## Requirements

- Python 3.x
- Git

## Installation

Clone the repository:

```bash
git clone https://github.com/laibasaf15/studenttaskmanager.git
```

Open the project folder:

```bash
cd studenttaskmanager
```

## Usage

Run the application:

```bash
python task_manager.py
```

The application displays a menu with the following options:

1. Add Task
2. Display Tasks
3. Complete Task
4. Delete Task
5. Exit

Follow the menu instructions to manage your tasks.

## Running Tests

Run the automated unit tests using:

```bash
python -m unittest discover -s tests -v
```

The tests cover task creation, empty-title validation, task completion, and task deletion.

## GitHub Actions

GitHub Actions automatically executes unit tests when code is pushed to the `main` branch or when a Pull Request targets `main`.

The workflow configuration is available at:

`.github/workflows/python-app.yml`

## Project Documentation

Additional user instructions are available in:

`docs/userguide.md`

## Version Control

The project uses Git branches to organize feature development. Pull Requests are used to review and merge changes into the main branch. Merge conflict resolution is also demonstrated in the repository history.

## Release

**Current Version: v1.0.0**

The first stable release of Student Task Manager is available on GitHub.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.