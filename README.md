# Documentation for project Duke (Developer guide)

> The whole project is based on the idea of `data saving` to the database and `data loading` from the database.  
  Both `console` and `web` applications use the` task object` and `database object` as main component.  
  However, `helper functions` are varied due the `different` usage.  
  All the `commands` inputted from the user, both from console and web, are set to `object` and store in the `Storage`.

## Console Application `duke-cli`
### Explanation
- The `entry point` of the console application is [duke-cli.py](\duke-cli.py).  
- Application can be `initialized` by running the following command.  
```bash
python duke-cli.py
```
- That will `run` the program and call the [start()](\console_model\start.py) function to print the `greeting message`.  
- And the program will initialize the `Storage` for tasks.  
- The `Storage object` is created by using a `class DB()` from [dataBase.py](database_model\dataBase.py).  
- A `list` with name `inputStringToList` is initialized to serve as a `temp storage` for incoming command.  
- A` while loop` is started and request for the `input` from the user.  
- While loop will run as long as the command` "bye"` is given.  
- The incoming `text` string is sparated by using [textSeparater()](console_model\extractor.py) function and then `stored` in the `inputStringToList` list.  
- Get the` command Type` from the `inputStringToList` with the help of [extractCommandType()](console_model\extractor.py) function.  
- Check for `command Type` and if `wrong`, call the [unknowCommand()](console_model\taskPrinter.py) function to acknowledge the user and `wait` for the command again.  
- If the command is `appropriate`, call the `function` with respect to the `command Type` by using the [extractFunction()](console_model\command_data.py) function.  
- Call [spaceDottedSpace()](console_model\taskPrinter.py) function for printing the `separation` between command.  
- When the user input the command `"bye"`, the loop is `exit` and call the [end()](\console_model\end.py) function at the end for printing the `ending texts` to the user.  


### Functions 
### Remark
> All the `modules` related to `console application` are stored in the [console_model](\console_model) folder.  
  All the `texts` for printing to user are `stored` in the [config.py](\console_model\config.py).  
  `Choice` in the [command_data.py](\console_model\command_data.py) module is the `dictonary` of `key` : command and `value` : higher order function.

### Print Helper Functions
| Module Name    | Function Name          | Input   | Return   |         Description                 |   
| ---------------| -----------------------| ------  | -------  | ------------------------------------|
| start.py       | `start()`              | `None`  | `None`   | Print the `greeting message`        |
| end.py         | `end()`                | `None`  | `None`   | Print` good bye message`            |
| taskPrinter.py | `printingDottedLine() `| `None`  | `None`   | Print `dotted line`                 |
| taskPrinter.py | ` spaceDottedSpace()`  | `None`  | `None`   | Skip one line and print dotted line |
| taskPrinter.py | `unknowCommand()`      | `None`  | `None`   | Print the unknown command message.  |
| taskPrinter.py | `dataBasePrinter() `   | `object`| `str`    | Take the `database object` and print the `count` of database in format |
| taskPrinter.py | `printTask() `         | `object`| `str`    | Take the `task object` and print the `task` in foramt according to the `command type`|
 
### Extractor Functions
| Module Name    | Function Name              | Input        | Return    |         Description          |
| ---------------| ---------------------------| -------------| ----------| -----------------------------|
| extractor.py   | `textSeparater()`          | `str`        |`list[str]`| Take the incoming `command text`, split it by `space` and return the `list of string` of command|
| extractor.py   | `extractCommandType()`     | `list[str]`  | `str`     | Take the `list of string` of command and return the `command type`  |
| extractor.py   | `extractCommandTitle()`    | `list[str]`  | `str`     | Take the `list of string` of command and return the `command title` |
| extractor.py   | `extractDeadLine()  `      | `list[str]`  | `str`     | Take the `list of string` of command and return the `due_time` |
| extractor.py   | `extractStartTimeForPlan()`| `list[str]`  | `str`     | Take the `list of string` of command and return the `start_time` |
| extractor.py   | `extractEndTimeForPlan()`  | `list[str]`  | `str`     | Take the `list of string` of command and return the `end_time`|
| extractor.py   | `extractTargetIdOfTask()`  | `list[str]`  | `int`     | Take the `list of string` of command and return the `id` from command |
| extractor.py   | `extractKeyWordOfTask()`   | `list[str]`  | `str`     | Take the `list of string` of command and return the `keyword` that user want to find |
| extractor.py   | `extractItem()   `         | `str`        | `str`     | Take the `command title` and return the` item name` |


### Action Functions
| Module Name          | Function Name              | Input        | Return    |         Description          |
| ---------------------| ---------------------------| -------------| ----------| -----------------------------|
| command_functions.py |`extractFunction()` | `dict[str,Any]`,`str`| `function` | Take in `dict` of action functions and command `key` and return the `higher order function` related to the inputed key|
| command_data.py| `TodoFunction()`    | `object`,`list[str]`| lambda function | `Flag`; Create `todo` object and store in the `Storage` and print the action done message and database count|
| command_data.py| `deadLineFunction()`| `object`,`list[str]`| lambda function | `Flag`; Create `deadline` object and store in the `Storage` and print the action done message and database count|
| command_data.py| `eventFunction()`   | `object`,`list[str]`| lambda function | `Flag`; Create `event` object and store in the `Storage` and print the action done message and database count|
| command_data.py| `listFunction()`    | `object`,`list[str]`| lambda function | `Flag`; Extract all the `tasks` from the `Storage` and print in the console|
| command_data.py| `markedFunction()`  | `object`,`list[str]`| lambda function | `Flag`; Extract the `task` by `id` from the `Storage` and `mark` the task and `True` and restore in the `Storage` |
| command_data.py| `unmarkedFunction()`| `object`,`list[str]`| lambda function | `Flag`; Extract the `task` by `id` from the `Storage` and `unmark` the task and `False` and restore in the `Storage`|
| command_data.py| `findFunction()`    | `object`,`list[str]`| lambda function | `Flag`; Extract all the `tasks` from the `Storage` which has the same `item name` as `keyword` in the `title` and display in `console`|
| command_data.py| `deleteFunction()`  | `object`,`list[str]`| lambda function | `Flag`; Remove the `task` by `id` from the `Storage` and display the` task delected` message |

##### Flag
> higher order functions are designed to take `database object` and `list of string of command` and perform the respective `action`.
##  

## Web Application `duke-web`
### Explanation
- The `entry point` of the web application is `duke-web.py`.  
- Application can be `initialized` by running the following command.  
```bash
flask --app duke-web.py run
```
- This will initialize the `duke web` `server` by running the [duke-web.py](duke-web.py).
- The interaction with client to server is connected via `5 end point` through `Flask`.
- As soon as the server is initialized, the `Stoarge` is created.
- The endpoint,` @app.get('/')` make sure the client to server connection is established.
- The first endpoint, `@app.get('/tasks')` is responsible for displying of the data. The function `list_or_find()` is 
responsible for displaying the data. It has `two features`; one is just listing all the element inside the database and the other is finding the data via `keyword`. This is done by changing the `task` `objects` stored in the database into `list of dict` and if no keyword is given, `all the data` are displayed. If the keyword is give, the tasks, item matching the keyword, will display.
- The second endpoint,` @app.post('/tasks')` is responsible for `creating` the task. It give the data inputted by the user in the `json` format. The function` create()` is requsting the data by using `request.json` and changed the data format to python dictionary and then to task object and stored in the database.
- The thrid endpoint, `@app.patch('/tasks/<int:id>/mark')`, is responsible for marking the task as `done`. The function` mark()` get the `task` by `id` from the database and set the `done` attribute of the task to `True`.
- The fouth endpoint, `@app.patch('/tasks/<int:id>/unmark')`, is responsible for marking the task as `not done`. The function `unmark()` get the `task` by `id` from the database and set the `done` attribute of the task to `False`.
- The fifth endpoint, `@app.delete('/tasks/<int:id>')`, is responsbile for `deleting` the task from the database. The function `delete()` remove the `task` by `id` from the database and `reset` the `id` of remaining tasks in the database.

### Example Data in Different Formats
Data in json
```json
{
  "type": "event",
  "payload": {
    "title": "IT5503 Lecture",
    "start_time": "Monday 7pm",
    "end_time": "Monday 9pm"
  }
}
```
Data in python Dictionary format
```python
{
  "type": "event",
  "title": "IT5503 Lecture",
  "start_time": "Monday 7pm",
  "end_time": "Monday 9pm",
  "id": 1,
  "done": False
  }
```


### Remark
> All the `modules` related to `web application` are stored in the [web_model](\assets\client) folder.  
  The web `client` is located in the `submodule` of the project `assets/client` folder.   
  The web server and client `interaction` is done by `Flask` API.  
  The important of this api is changing the data in `json` format to python `dictionary` format for displaying and `task object` for displaying.

### Functions 

### Operation Functions
| Module Name          | Function Name   | Input   | Return  |         Description          |
| ---------------------| ----------------| --------| --------| -----------------------------|
| operationFunctions.py| `markTask()`    | `object`| `None`  | Set the `done` of the task object to `True`|
| operationFunctions.py| `unmarkTask()`  | `object`| `None`  | Set the `done` of the task object to `False`|
### Formatter Functions
| Module Name  | Function Name      | Input         | Return    |         Description          |
| -------------| -------------------| ------------- | ----------| -----------------------------|
| formatter.py | `dataFormatter()`  | `dict{}`,`int`| `dict{}`  | Change the `data` in `json` format into python dictionary `format`|

### Task to Object Translation Functions
| Module Name           | Function Name | Input   | Return    |         Description          |
| --------------------- | --------------| --------| ----------| -----------------------------|
| dictToObjFormatter.py | `dictToObj()` | `dict{}`| `object`  | Take data in dictionary format and create the `task` object according to the `command type`|


### Object to Task Translation Functions
| Module Name          | Function Name             | Input   | Return    |         Description          |
| ---------------------| --------------------------| --------| ----------| -----------------------------|
| objToDictFormatter.py| `taskToDict()`            | `object`|`dict{}`   | Change the `task` object into python `dictionary` format|
| objToDictFormatter.py| `taskWithDueTimeToDict()` | `object`| `dict{}`  | Change the `task with due_time` object into python `dictionary` format|
| objToDictFormatter.py| `taskWithPlanToDict()`    | `object`| `dict{}`  | Change the `task with plan` object into python `dictionary` format|
| objToDictFormatter.py| `objToDict()`             | `object`| `dict{}`  | Change the `task` into python `dictionary` format accordingly|
| objToDictFormatter.py| `makeDictsList()`         | `object`| `list[]`  | Change `all the tasks object` in the database into python `dictionary` format|
##   


## Application tester `duke-test`
> Duke tester is for testing the `functionality` of the `duke-cli.py`.  
  Testing is performed by using the `unitest` module of the python.
### Explanation
- The `entry point` of the duke tester is [duke-test.py](\duke-test.py).  
- Application can be `initialized` by running the following command.  
```bash
python duke-test.py
```
- This will run the [duke-test.py](\duke-test.py).
- Inside the [duke-test.py](\duke-test.py), the `class TestTaskManager` is exit.  
- By running the `tester`, this will start testing on `6` different testing functions of `duke-cli.py`
- Testing the creating of task `todo` and storing in `database`.
- Testing the creating of task `deadline` and storing in `database`.
- Testing the creating of task `event` and storing in `database`.
- Testing the `mark` condition by setting `True` to the `done` attribute of the `task object` by `id` and store back in `database`.
- Testing the `unmark` condition by setting `False` to the `done` attribute of the `task object` by `id` and store back in `database`.
- Testing the `removing` the` task object` by `id` from the `database`.


### Functions 

### Test Functions
| Function Name               | Input  | Return |         Description                                                  |
| ----------------------------|--------| -------| ---------------------------------------------------------------------|
| `test_add_todo()`           | `self` | `None` | Test the functionality of `TodoFunction()` in console application    |
| `test_add_deadline()`       | `self` | `None` | Test the functionality of `deadLineFunction()` in console application|
| `test_add_event()`          | `self` | `None` | Test the functionality of `eventFunction()` in console application   |
| `test_mark_task_as_done()`  | `self` | `None` | Test the functionality of `markedFunction()` in console application  |
| `test_unmark_task_as_done()`| `self` | `None` | Test the functionality of `unmarkedFunction()` in console application|
| `test_delete_task()`        | `self` | `None` | Test the functionality of `deleteFunction()` in console application  |

### Remark
> Testing on functions is done by using the `assertEqual() ` method of the `unitest` module and
 also utilize the `same structure` used in `duke-cli.py`.  
 Database object is create with the name `Storage`.

##   

## Classes
> This the `foundation` of the project.  
  All the `commands` inputted by the users are changed into `task` object.   
  `Formatting` is done with the help of `helper` functions.  
  In `console` application, the` text strings` inputted by user are breaked by `space` and set to the `attribute` of the class respectively.  
  In `web` application, the `json` formatted data, received from the API via end point `@app.post('/tasks')` is changed into task object's `attribute`.
  The `Storage` is created by using the `DB() class` which is also the heart of the project.  
  All the `tasks` are stored in the `Storage` object.

### Remark
> All the `modules` related to `task` are stored in the `task.py` module in the [task_model](\task_model\task.py) folder. 
> All the `attributes` of the classes are `private`.
### Task Class
- This class is used to create `todo` task object.

#### Attributes 
| Attribute Name | Data Type |
| ---------------|-----------| 
| __type         |`str`      |
| __title        |`str`      |
| __done         |`str`      |
| __symbol       |`str`      |
| __id           |`int`      |  
  
#### Getter and Setter
| Function Name       | Input      | Return |         Description                  |
| --------------------|--------    | -------| -----------------------------------  |
| `setType()`         |`self`,`str`|`None`    | Set the `type` of the task         |
| `setTitle()`        |`self`,`str`|`None`    | Set the `title` of the task        |
| `setSymbol()`       |`self`,`str`|`None`    | Set the `symbol` of the task       |
| `markedTask()`      |`self`      |`None`    | Set the `done` of the task to `True` |
| `unmarkedTask()`    |`self`      |`None`    | Set the `done` of the task to `False`|
| `setId()`           |`self`,`int`|`None`    | Set the `id` of the task           |
| `getType()`         |`self`      |`str`     | Get the `type` of the task         |
| `getTitle()`        |`self`      |`str`     | Get the `title` of the task        |
| `getSymbol()`       |`self`      |`str`     | Get the `symbol` of the task       |
| `getDoneCondition()`|`self`      |`bool`    | Get the `done` of the task         |
| `getId()`           |`self`      |`int`     | Get the `id` of the task           |


### Task with DueTime
- This class is used to create `deadline` task object.
- Inherited from the parent class `Task()`

#### Attributes 
| Attribute Name | Data Type |
| ---------------|-----------| 
| __dueTime      |`str`      |

  
#### Getter and Setter
| Function Name     | Input      | Return |         Description              |
| ------------------|--------    | -------| -------------------------------  |
| `setDueTime()`    |`self`,`str`|`None`  | Set the `due time` of the task   |
| `getDueTime()`    |`self`      |`str`   | Get the `due time` of the task   |


### Task with plan
- This class is used to create `event` task object.
- Inherited from the parent class `Task()`
#### Attributes 
| Attribute Name | Data Type |
| ---------------|-----------| 
| __startTime    |`str`      |
| __endTime      |`str`      |

  
#### Getter and Setter
| Function Name     | Input      | Return   |         Description                |
| ----------------  |--------    | -------  | ---------------------------------  |
| `setStartTime()`  |`self`,`str`|`None`    | Set the `start time` of the plan   |
| `setEndTime()`    |`self`,`str`|`None`    | Set the `end time` of the plan     |
| `getStartTime()`  |`self`      |`str`     | Get the `start time` of the plan   |
| `getEndTime()`    |`self`      |`str`     | Get the `end time` of the plan     |



### Database Class
> This is the `database` of the project for storing the `tasks`.
> The database is base on the` list[]` for flexibility of saving and loading of data.
### Remark
> All the `modules` related to `database` are stored in the `dataBase.py` module in the [database_model](\task_model\task.py) folder.  

#### Attributes 
| Attribute Name | Data Type |
| ---------------|-----------| 
| __storage      |`str`      |
| __count        |`int`      |
 
#### Getter and Setter
| Function Name | Input          | Return |         Description                             |
| --------------|----------------| -------| ------------------------------------------------|
| `addItem()`     |`self`,`object`   |`None`    | Adding item to the `list`, database storage       |
| `getItem()`     |`self`,`int`      |`object`  | Loading item from the `list`, database storage    |
| `getCount()`    |`self`            |`int`     | Get the total `count` of the item in the database |
| `removeItem()`  |`self`,`int`      |`object`  | Remove the `item` from the database               |
| `getStorage()`  |`self`            |`list[]`  | Get the `whole storage` of the database           |
| `clearStorage()`|`self`            |`None`    | Delete `all the data` from the database           |