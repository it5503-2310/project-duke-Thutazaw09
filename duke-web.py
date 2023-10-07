from flask import Flask, send_from_directory, request
from typing import Any
from web_model import formatter, dictToObjFormatter, objToDictFormatter, operationFunctions
from database_model import dataBase

app = Flask(__name__, static_url_path='', static_folder='assets/client')

Storage = dataBase.DB()
Storage.clearStorage()


@app.get('/')
def serve_client():
    return send_from_directory('assets/client', 'index.html')


@app.get('/tasks')
def list_or_find() -> Any:
    keyword = request.args['find']
    listOfTasks: list[Any] = objToDictFormatter.makeDictsList(
        Storage)  # type: ignore
    if keyword != "":
        returnTaskList: list[dict[str, Any]] = []
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
        lengthOfData: int = Storage.getCount()
        for i in range(lengthOfData):
            current_id = i + 1

        dataDict = formatter.dataFormatter(data, current_id)
        dataObj = dictToObjFormatter.dictToObj(dataDict)
        Storage.addItem(dataObj)
        return ''
    except:
        return ''


@app.patch('/tasks/<int:id>/mark')
def mark(id: int):
    taskToMark = Storage.getItem(id)
    operationFunctions.markTask(taskToMark)
    return ''


@app.patch('/tasks/<int:id>/unmark')
def unmark(id: int):
    taskToUnMark = Storage.getItem(id)
    operationFunctions.unmarkTask(taskToUnMark)
    return ''


@app.delete('/tasks/<int:id>')
def delete(id: int):
    Storage.remmoveItem(id)
    for i in range(Storage.getCount()):
        tsk = Storage.getItem(i)
        tsk.setId(i)
    return ''
