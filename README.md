# Documentation for project Duke (Developer guide)

> The whole project is based on the idea of `data saving` to the database and `data loading` from the database.  
  Both `console` and `web` applications use the` task object` and `database object` as main component.  
  However, `helper functions` are varied due the `different` usage.

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
- This will initialize the `web` `server` by running the [duke-web.py](duke-web.py).





baldsca faaj sldfjha sdd

a
sd fasdf 
ads
f a
sdf 
asdf

Neeed  to add explanation 



### Remark
> All the `modules` related to `web application` are stored in the [web_model](\assets\client) folder.  
  The web `client` is located in the `submodule` of the project `assets/client` folder.   
  The web server and client `interaction` is done by `Flask` API.

### Functions 

### Operation Functions
| Module Name          | Function Name              | Input        | Return    |         Description          |
| ---------------------| ---------------------------| -------------| ----------| -----------------------------|
### Formatter Functions
| Module Name          | Function Name              | Input        | Return    |         Description          |
| ---------------------| ---------------------------| -------------| ----------| -----------------------------|
### Task to Object Translation Functions
| Module Name          | Function Name              | Input        | Return    |         Description          |
| ---------------------| ---------------------------| -------------| ----------| -----------------------------|
### Object to Task Translation Functions
| Module Name          | Function Name              | Input        | Return    |         Description          |
| ---------------------| ---------------------------| -------------| ----------| -----------------------------|

dict structture adnfa sdfa sdfakls dfalsjd fal;ksdjf a;lksdjfl



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
> The applications are created  asdf asdf asdf asdf asdf asdfa sdfasdf asdf asdf






### Remark
> All the `modules` related to `task` are stored in the `task.py` module in the [task_model](\task_model\task.py) folder. 

### Task Class
> dadsjf lasdjfa losd fjalksdkf alksd
### Task with DueTime
> dadsjf lasdjfa losd fjalksdkf alksd
### Task with plan
> dadsjf lasdjfa losd fjalksdkf alksd
### Database Class
> dadsjf lasdjfa losd fjalksdkf alksd


### Remark
> All the `modules` related to `database` are stored in the `dataBase.py` module in the [database_model](\task_model\task.py) folder.  

