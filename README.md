# proj-duke

Project Duke is an educational software project designed to take you through the steps of building a small software incrementally, while applying software engineering techniques as possible along the way.

The project aims to build a product named Duke, a Personal Assistant Chatbot that helps a person to keep track of various things. The name Duke was chosen as a placeholder name, in honor of Duke, the Java Mascot, which is the language used in the SE textbook. We will instead be using Python.

## Sample Interaction with Duke
> ```
> Hello! I'm Duke
> What can I do for you?
> ---------------------------------
>
> > todo borrow book
> ---------------------------------
> Got it. I've added this task:
>   [T][ ] borrow book
> Now you have 1 tasks in the list.
>
> ---------------------------------
>
> > deadline return book /by Sunday
> ---------------------------------
> Got it. I've added this task:
>   [D][ ] return book (by: Sunday)
> Now you have 2 tasks in the list.
>
> ---------------------------------
>
> > event project meeting /from Mon 2pm /to 4pm
> ---------------------------------
> Got it. I've added this task:
>   [E][ ] project meeting (from: Mon 2pm to: 4pm)
> Now you have 3 tasks in the list.
>
> ---------------------------------
>
> > list
> ---------------------------------
> Here are the tasks in your list:
> 1.  [T][ ] borrow book
> 2.  [D][ ] return book (by: Sunday)
> 3.  [E][ ] project meeting (from: Mon 2pm to: 4pm)
>
> ---------------------------------
>
> > mark 1
> ---------------------------------
> Nice! I've marked this task as done:
>   [T][X] borrow book
>
> ---------------------------------
>
> > unmark 1
> ---------------------------------
> OK, I've marked this task as not done yet:
>   [T][ ] borrow book
>
> ---------------------------------
>
> > find book
> ---------------------------------
> Here are the matching tasks in your list:
>   [T][ ] borrow book
>   [D][ ] return book (by: Sunday)
>
> ---------------------------------
>
> > delete 2
> ---------------------------------
> Noted. I've removed this task:
>   [D][ ] return book (by: Sunday)
> Now you have 2 tasks in the list.
>
> ---------------------------------
>
> > list
> ---------------------------------
> Here are the tasks in your list:
> 1.  [T][ ] borrow book
> 2.  [E][ ] project meeting (from: Mon 2pm to: 4pm)
>
> ---------------------------------
>
> > blah
> ---------------------------------
> OOPS!!! I'm sorry, but I don't know what that means :(
>
> ---------------------------------
>
> todo
> ---------------------------------
> OOPS!!! The description of a todo cannot be empty
>
> ---------------------------------
>
> > bye
> ---------------------------------
> Bye. Hope to see you again soon!
> ```

## Types of Tasks

There are three types of tasks:
1. Todos: tasks without any date/time attached to it e.g., visit new theme park
2. Deadlines: tasks that need to be done before a specific date/time e.g., *submit report by 11/10/2019 5pm*
3. Events: tasks that start at a specific date/time and ends at a specific date/time
e.g., (a) *team project meeting 2/10/2019 2-4pm (b) orientation week 4/10/2019 to 11/10/2019*

For now, date/time can be treated as a string.

## Other Commands
Tasks can be marked as done using the command `mark` and unmarked using `unmark`.
They can also be deleted with the `delete` command.

The command `find` give users a way to find a task by searching for a keyword. `list` simply lists all tasks.

## Persistency

Save the tasks in the hard disk automatically whenever the task list changes. Load the data from the hard disk when the chatbot starts up. You may hard-code the file name and relative path from the project root e.g., ./data/duke.txt

The format of the file is up to you.