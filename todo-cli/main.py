import click  # Importing Click for command-line interface (CLI) functionality
import os  # Importing OS module to check file existence
import json  # Importing JSON module to handle task storage in JSON format

# Define the file where tasks will be stored
Todolist = "todo.json"

# Function to load tasks from the JSON file
def load_task():
    if not os.path.exists(Todolist):  # Check if the file exists
        return []  # Return an empty list if the file doesn't exist
    with open(Todolist, 'r') as file:  # Open the file in read mode
        try:
            return json.load(file)  # Load tasks from the JSON file
        except json.JSONDecodeError:  # Handle case if file is empty or corrupted
            return []  # Return an empty list

# Function to save tasks to the JSON file
def save_task(task):
    with open(Todolist, 'w') as file:  # Open the file in write mode
        json.dump(task, file, indent=4)  # Save tasks to the file with indentation

# Define a Click group to manage commands
@click.group()
def cli():
    """A simple todo list"""
    pass  # Placeholder function for grouping commands

# Command to add a new task
@click.command()
@click.argument('task')  # Take task as an argument from the user
def add(task):
    """Add a new task to the list"""
    tasks = load_task()  # Load existing tasks
    tasks.append({"task": task, "done": False})  # Append new task with status "not done"
    save_task(tasks)  # Save the updated task list
    click.echo(f"✅ Task added Successfully: {task}")  # Print success message

# Command to list all tasks
@click.command(name="list")  # Avoids conflict with Python's built-in list function
def list_tasks():
    """List all tasks"""
    tasks = load_task()  # Load tasks from the file
    if not tasks:  # If no tasks found
        click.echo("📂 No task found")  # Display message
        return
    for i, task in enumerate(tasks, 1):  # Loop through tasks and number them
        status = "✅" if task["done"] else "❌"  # Mark completed tasks
        click.echo(f"{i}. [{status}] {task['task']}")  # Print task with status

# Command to mark a task as completed
@click.command()
@click.argument('task_number', type=int)  # Accept task number as an argument
def complete(task_number):
    """Mark a task as completed"""
    tasks = load_task()  # Load tasks from file
    try:
        tasks[task_number - 1]["done"] = True  # Mark the specified task as completed
        save_task(tasks)  # Save updated tasks
        click.echo(f"🎯 Task {task_number} marked as completed")  # Print success message
    except IndexError:  # Handle invalid task number
        click.echo("⚠️ Invalid task number")  # Display error message

# Command to delete a task
@click.command()
@click.argument('task_number', type=int)  # Accept task number as an argument
def delete(task_number):
    """Delete a task"""
    tasks = load_task()  # Load tasks from file
    try:
        del tasks[task_number - 1]  # Delete the specified task
        save_task(tasks)  # Save updated tasks
        click.echo(f"🗑️ Task {task_number} deleted")  # Print success message
    except IndexError:  # Handle invalid task number
        click.echo("⚠️ Invalid task number")  # Display error message

# Add commands to the CLI group
cli.add_command(add)
cli.add_command(list_tasks, name="list")  # Alias 'list_tasks' command as 'list'
cli.add_command(complete)
cli.add_command(delete)

# Run the CLI application when executed
if __name__ == '__main__':
    cli()
