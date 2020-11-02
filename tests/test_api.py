__author__ = "Rohan Singh"
from todo.api import add_task_to_db, list_tasks, delete_task, finish_task


def test_list_tasks(test_app):
    assert list_tasks() == [], "tasks found in testdb"

    # now add some tasks
    add_task_to_db("task from test 1")
    add_task_to_db("task from test 2")

    assert len(list_tasks()) == 2


def test_add_task(test_app):
    assert len(list_tasks()) == 0
    add_task_to_db("task3")
    assert len(list_tasks()) == 1


def test_delete(test_app):
    add_task_to_db("delete test")
    delete_task(1)
    assert list_tasks() == []


def test_finish_task(test_app):
    add_task_to_db("finish this now")
    finish_task(1)
    assert list_tasks()[0].done is not False
