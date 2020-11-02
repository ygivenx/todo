"""URLs for our application."""

from todo import app
from flask import render_template
from flask import request, redirect
from todo.api import add_task_to_db, list_tasks, delete_task, finish_task

# TODO: Write URLs for the application


@app.route("/")
def task_list():
    """
    Create a route for base address

    :return: application page
    """
    tasks = list_tasks()
    return render_template("application.html", tasks=tasks)


@app.route("/task", methods=["POST"])
def add_task():
    """
    Define route for task

    :return: application page
    """
    task = request.form["body"]
    if task is None:
        raise Exception("Empty task")
    else:
        add_task_to_db(task)

    return redirect("/")


@app.route("/done/<id>")
def complete_task(id):
    """
    Route to mark a task complete

    :param id: ID for task to be completed
    :return: application page
    """
    finish_task(id)
    return redirect("/")


@app.route("/delete/<id>")
def remove_task(id):
    """
    Route to mark delete a task

    :param id: ID of task to be deleted
    :return: application page
    """
    delete_task(id)
    return redirect("/")
