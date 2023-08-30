
from task import Task
from database import DB

data = DB()


t1 = Task("todo")
t2 = Task("deadline")
t3 = Task("event")
data.addTask(t1)
data.addTask(t2)
data.addTask(t3)
print(data.storage)
print(data.countTask())
print(data.showTask(1).command)


