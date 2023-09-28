from flask import Flask, send_from_directory
from typing import Any
app = Flask(__name__, static_url_path='', static_folder='assets/client')

task_list:list[dict[str,Any]] = [
    {
        "id" : 0,
        "done" : False,
        "type" : "todo",
        "title" : "Borrow book"
    },
    {
        "id" : 1,
        "done" : True,
        "type" : "deadline",
        "title" : "Return book",
        "due_time" : "Monday"
    },
    {
        "id" : 2,
        "done" : False,
        "type" : "event",
        "title" : "Meeting",
        "start_time" : "2pm",
        "end_time" : "4pm"
    }
]

@app.get('/')
def list_or_find():
    return send_from_directory('assets/client', 'index.html')


@app.post('/tasks')
def create():
    print("Creting task")
    return task_list

@app.patch('/tasks/<int:id>/mark')
def mark(id: int):
    return ''


@app.patch('/tasks/<int:id>/unmark')
def unmark(id: int):
    return ''

@app.delete('/tasks/<int:id>')
def delete(id: int):
    return ''
