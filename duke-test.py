import unittest
from console_model import  extractor, command_data
from task_model import task
from database_model import dataBase
from io import StringIO
import sys

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        # Create a TaskManager instance for testing
        self.task = task.Task()
        self.taskWithDueTime = task.TaskWithDueTime()
        self.taskWithPlan = task.TaskWithPlan()
        self.Storage = dataBase.DB()
        self.stdout = StringIO()
        sys.stdout = self.stdout
        
    def tearDown(self) -> None:
        sys.stdout = sys.__stdout__

    def test_add_todo(self):
        # Test adding a "todo" task
        testString = "todo borrow book"
        inputStringToList = extractor.textSeparater(testString)
        commandType = extractor.extractCommandType(inputStringToList)
        action = command_data.extractFunction(
            command_data.choice, commandType)  # type: ignore
        action(self.Storage, inputStringToList)
        self.assertEqual(self.Storage.getCount(), 1)

    def test_add_deadline(self):
        # Test adding a "deadline" task
        testString = "deadline return book /by Sunday"
        inputStringToList = extractor.textSeparater(testString)
        commandType = extractor.extractCommandType(inputStringToList)
        action = command_data.extractFunction(
            command_data.choice, commandType)  # type: ignore
        action(self.Storage, inputStringToList)
        self.assertEqual(self.Storage.getCount(), 1)

    def test_add_event(self):
        # Test adding an "event" task
        testString = "event project meeting /from Mon 2pm /to 4pm"
        inputStringToList = extractor.textSeparater(testString)
        commandType = extractor.extractCommandType(inputStringToList)
        action = command_data.extractFunction(
            command_data.choice, commandType)  # type: ignore
        action(self.Storage, inputStringToList)
        self.assertEqual(self.Storage.getCount(), 1)

    def test_mark_task_as_done(self):
        # Test marking a task 
        # adding a task to database
        testString = "todo borrow book"
        inputStringToList = extractor.textSeparater(testString)
        commandType = extractor.extractCommandType(inputStringToList)
        action = command_data.extractFunction(
            command_data.choice, commandType)  # type: ignore
        action(self.Storage, inputStringToList)
        # marking the test
        markTask = "mark 1"
        inputStringToList = extractor.textSeparater(markTask)
        commandType = extractor.extractCommandType(inputStringToList)
        action = command_data.extractFunction(
            command_data.choice, commandType)  # type: ignore
        action(self.Storage, inputStringToList)
        taskToMark = self.Storage.getItem(0)
        self.assertTrue(taskToMark.getDoneCondition())

    def test_unmark_task_as_done(self):
        # Test unmarking a task 
        # adding a task to database
        testString = "todo borrow book"
        inputStringToList = extractor.textSeparater(testString)
        commandType = extractor.extractCommandType(inputStringToList)
        action = command_data.extractFunction(
            command_data.choice, commandType)  # type: ignore
        action(self.Storage, inputStringToList)
        # marking the test
        markTask = "mark 1"
        inputStringToList = extractor.textSeparater(markTask)
        commandType = extractor.extractCommandType(inputStringToList)
        action = command_data.extractFunction(
            command_data.choice, commandType)  # type: ignore
        action(self.Storage, inputStringToList)
        # unmarking the test
        markTask = "unmark 1"
        inputStringToList = extractor.textSeparater(markTask)
        commandType = extractor.extractCommandType(inputStringToList)
        action = command_data.extractFunction(
            command_data.choice, commandType)  # type: ignore
        action(self.Storage, inputStringToList)
        taskToUnMark = self.Storage.getItem(0)
        self.assertFalse(taskToUnMark.getDoneCondition())

    def test_delete_task(self):
        # Test deleting a task
        # adding tasks to the data base
        # task1
        testString = "todo borrow book"
        inputStringToList = extractor.textSeparater(testString)
        commandType = extractor.extractCommandType(inputStringToList)
        action = command_data.extractFunction(
            command_data.choice, commandType)  # type: ignore
        action(self.Storage, inputStringToList)
        # task2 
        testString = "deadline return book /by Sunday"
        inputStringToList = extractor.textSeparater(testString)
        commandType = extractor.extractCommandType(inputStringToList)
        action = command_data.extractFunction(
            command_data.choice, commandType)  # type: ignore
        action(self.Storage, inputStringToList)
        # task 3
        testString = "event project meeting /from Mon 2pm /to 4pm"
        inputStringToList = extractor.textSeparater(testString)
        commandType = extractor.extractCommandType(inputStringToList)
        action = command_data.extractFunction(
            command_data.choice, commandType)  # type: ignore
        action(self.Storage, inputStringToList)
        
        # delete task with id 1
        testString = "delete 1"
        inputStringToList = extractor.textSeparater(testString)
        commandType = extractor.extractCommandType(inputStringToList)
        action = command_data.extractFunction(
            command_data.choice, commandType)  # type: ignore
        action(self.Storage, inputStringToList)
        self.assertEqual(self.Storage.getCount(), 2)


if __name__ == '__main__':
    unittest.main()
