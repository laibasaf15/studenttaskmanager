# Student Task Manager - Lab Report

## 1. Introduction

The Student Task Manager is a Python-based console application developed to help students manage their academic tasks. This project demonstrates the use of Git and GitHub for version control and project management.

## 2. Objectives

- Understand Git and GitHub.
- Create and manage branches.
- Track changes through meaningful commits.
- Use GitHub Issues and Pull Requests.
- Create and resolve merge conflicts.
- Perform automated unit testing.
- Configure GitHub Actions.
- Publish a GitHub Release.

## 3. Technologies Used

- Python
- Git
- GitHub
- Python unittest
- GitHub Actions
- Visual Studio Code

## 4. Application Features

- Add new tasks.
- Display all tasks.
- Complete pending tasks.
- Delete tasks.
- Validate empty task titles.
- Maintain unique task IDs.

## 5. Version Control

Git was used to track project changes. Three feature branches were created:

- `feature/addtask`
- `feature/completetask`
- `feature/deletetask`

Meaningful commits were created to document development progress. Changes were integrated into the main branch using Pull Requests.

## 6. GitHub Issues and Pull Requests

Four GitHub Issues were created to organize and track project tasks. Five Pull Requests were created, reviewed, and successfully merged into the main branch.

## 7. Merge Conflict Resolution

A merge conflict was intentionally created by modifying the same project status line differently in two branches.

The conflict was identified using Git conflict markers and resolved manually. The corrected version was committed and pushed to GitHub.

## 8. Unit Testing

Python's unittest framework was used to test the application.

Four test cases were implemented:

- Adding a task.
- Rejecting an empty task.
- Completing a task.
- Deleting a task.

Tests were executed using:

`python -m unittest discover -s tests -v`

All four tests passed during local testing.

## 9. GitHub Actions

A GitHub Actions workflow was configured to run unit tests automatically when code is pushed to the main branch or when a Pull Request targets main.

The workflow was used to demonstrate successful and failed test executions.

## 10. GitHub Release

The project was published as version `v1.0.0` on GitHub.

## 11. Conclusion

This project provided practical experience with Git, GitHub, branching, commits, Issues, Pull Requests, merge conflict resolution, unit testing, and continuous integration. It demonstrated how version control helps organize and manage software development.