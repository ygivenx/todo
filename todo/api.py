"""API functions to interact with TODO tasks."""

from todo import db
from todo.models import TODO

# TODO: Write functions to list/create/delete/finish tasks


def list_tasks():
    """
    List all the tasks in the database

    :return: Task list
    """
    return TODO.query.all()


def add_task_to_db(task):
    """
    Add a new task to Database

    :param task: the task description
    :return: None
    """
    new_task = TODO(body=task)
    db.session.add(new_task)
    db.session.commit()


def delete_task(task_id):
    """
    Delete a task from database

    :param task_id: ID of task to be deleted
    :return: None
    """
    TODO.query.filter_by(id=task_id).delete()
    db.session.commit()


def finish_task(task_id):
    """
    Mark a task completed

    :param task_id: ID of task to be marked completed
    :return: None
    :return: None
    """
    item = TODO.query.filter_by(id=task_id).first()
    item.done = 1
    db.session.commit()
