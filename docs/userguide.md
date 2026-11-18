
# Student Task Manager - User Guide

## Introduction

Student Task Manager is a simple console-based Python application designed to help students organize their academic tasks.

## Starting the Application

Open PowerShell in the project directory and run:

```bash
python task_manager.py
```

## Adding a Task

1. Select option 1.
2. Enter the task title.
3. The application confirms successful addition.
4. Empty task titles are not accepted.

## Displaying Tasks

1. Select option 2.
2. All saved tasks are displayed with their IDs and statuses.

## Completing a Task

1. Select option 3.
2. Enter the task ID.
3. The task status changes to Completed.

## Deleting a Task

1. Select option 4.
2. Enter the task ID.
3. The selected task is deleted.

## Exiting

Select option 5 to close the application.

## Running Tests

Use this command to run the automated tests:

```bash
python -m unittest discover -s tests -v
```
