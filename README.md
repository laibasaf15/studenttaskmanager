
# Student Task Manager

A simple Python console application that helps students manage their tasks.

## Features

- Add new tasks.
- Display all tasks.
- Complete pending tasks.
- Delete tasks.
- Validate empty task titles.
- Maintain unique task IDs.
- Automated unit testing using GitHub Actions.

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

Choose an option from the menu:

1. Add Task
2. Display Tasks
3. Complete Task
4. Delete Task
5. Exit

## Running Tests

Run the unit tests using:

```bash
python -m unittest discover -s tests -v
```

## GitHub Actions

GitHub Actions automatically runs unit tests whenever code is pushed to the main branch or a pull request targets main.

## License

This project is licensed under the MIT License.
