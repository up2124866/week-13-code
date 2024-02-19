from tkinter import *
from backend import *

class ToDoListApp:

    def __init__(self, taskList):
        self.taskList = taskList
        self.win = Tk()
        self.win.title("To Do List App")

        self.mainframe = Frame(self.win)
        self.mainframe.grid(
            padx=5,
            pady=5
        )

        self.newTask = StringVar()
        self.newTask.set("New Task")

        self.editTask =  StringVar()
        self.editTask.set("Edited Task")


        self.taskWidget = []

    def createWidgets(self):
        self.deleteAllWidgets()
        for i in range(self.taskList.getNumTasks()):
            taskLabel = Label(
                self.mainframe,
                text=self.taskList.getTaskMsgByIndex(i)
            )
            taskLabel.grid(
                column=0,
                row=i,
                padx=5,
                pady=5,
                sticky=W
            )
            self.taskWidget.append(taskLabel)



            editButton = Button(
                self.mainframe,
                text="Edit",
                command=lambda index=i: self.createNewWin(index)
            )
            editButton.grid(
                column=1,
                row=i,
                padx=5,
                pady=5
            )
            self.taskWidget.append(editButton)



            deleteButton = Button(
                self.mainframe,
                text="Delete",
                command= lambda index=i: self.deleteTask(index)
            )
            deleteButton.grid(
                column=2,
                row=i,
                padx=5,
                pady=5
            )
            self.taskWidget.append(deleteButton)
        
        bugFixFrame = Frame(self.mainframe)
        bugFixFrame.grid(column=0, row=i+1, padx=5, pady=5)

        newTaskEntry = Entry(
            bugFixFrame,
            width=20,
            textvariable=self.newTask
        )
        newTaskEntry.grid()
        self.taskWidget.append(newTaskEntry)



        addTaskButton = Button(
            self.mainframe,
            text="Add",
            command=self.addTask
        )
        addTaskButton.grid(
            column=1,
            row=i+1,
            padx=5,
            pady=5,
            columnspan=2
        )
        self.taskWidget.append(addTaskButton)
        
    def createNewWin(self, index):
        self.newWin = Toplevel(
            self.win,
            padx=5,
            pady=5
        )
        self.newWin.title("Edit Task")

        editTaskEntry = Entry(
            self.newWin,
            textvariable=self.editTask,
            width=20
        )
        editTaskEntry.grid(
            column=0,
            row=0,
            padx=5,
            pady=5
        )


        submitTaskButton = Button(
            self.newWin,
            text="Submit",
            command=lambda: self.editTaskAtIndex(index)
        )
        submitTaskButton.grid(
            column=1,
            row=0,
            padx=5,
            pady=5
        )

    def deleteTask(self, index):
        self.taskList.removeTaskAtIndex(index)
        self.createWidgets()

    def deleteAllWidgets(self):
        for widget in self.taskWidget:
            widget.destroy()
        self.taskWidget = []

    def editTaskAtIndex(self, index):
        self.taskList.setTaskMsgAtIndex(index, self.editTask.get())
        self.createWidgets()
        self.newWin.destroy()

    def addTask(self):
        self.taskList.addTaskByMsg(self.newTask.get())
        self.createWidgets()

    def run(self):
        self.createWidgets()
        self.win.mainloop()

myList = TaskList()

myList.addTaskByMsg("Buy milk")
myList.addTaskByMsg("Buy water")
myList.addTaskByMsg("Buy eggs")

myApp = ToDoListApp(myList)
myApp.run()