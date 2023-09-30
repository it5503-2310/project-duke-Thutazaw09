from flask import Flask, send_from_directory, request
from typing import Any
from web_model import dataHandler
from database_model import dataBase

app = Flask(__name__, static_url_path='', static_folder='assets/client')

Storage = dataBase.DB()

@app.get('/')
def serve_client():
    return send_from_directory('assets/client', 'index.html')

@app.get('/tasks')
def list_or_find() -> Any:
    keyword = request.args['find']
    listOfTasks = Storage.getStorage()
    if keyword != "":
        returnTaskList: list[dict[str, Any]] = []  # function 1 khu htae ml
        for item in listOfTasks:
            if keyword in item["title"]:
                returnTaskList.append(item)
        return returnTaskList
    return listOfTasks

@app.post('/tasks')
def create():
    # Getting data from the input
    try:
        data: Any = request.json
        current_id = 0
        lengthOfData:int = Storage.getCount()
        for i in range(lengthOfData):
          current_id = i + 1
        dataDict = dataHandler.dataFormatter(data,current_id)
        Storage.addItem(dataDict)
        return ''
    except:
        return ''


@app.patch('/tasks/<int:id>/mark')
def mark(id: int):
    tastToMark = Storage.getItem(id)
    dataHandler.markTask(tastToMark)
    return ''


@app.patch('/tasks/<int:id>/unmark')
def unmark(id: int):
    tastToUnMark = Storage.getItem(id)
    dataHandler.unmarkTask(tastToUnMark)
    return ''


@app.delete('/tasks/<int:id>')
def delete(id: int):
    Storage.remmoveItem(id)
    return ''


