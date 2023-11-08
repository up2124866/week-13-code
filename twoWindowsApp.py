from tkinter import *


class App:
    def __init__(self):
        self.win = Tk()
        self.win.title("Main Window")
        
        self.num = IntVar()
        self.num.set(12)

    def run(self):
        self.createWidgets()
        self.win.mainloop()

    def createWidgets(self):
        numberLabel = Label(
            self.win,
            text=f"Number: {self.num.get()}"
        )
        numberLabel.pack()

        updateButton = Button(
            self.win,
            text="Update number",
            command=lambda: self.createNewWindow(numberLabel)
        )
        updateButton.pack()

    def createNewWindow(self, numberLabel):
        newWindow = Toplevel(self.win)
        newWindow.title("Update number")

        newNumEntry = Entry(
            newWindow,
            textvariable=self.num
        )
        newNumEntry.pack()

        newNumButton = Button(
            newWindow,
            text="Update number",
            command=lambda: self.updateNum(numberLabel, newWindow)
        )
        newNumButton.pack()

    def updateNum(self, numberLabel, newWindow):
        numberLabel.config(text=f"Number: {self.num.get()}")
        newWindow.destroy()


def main():
    app = App()
    app.run()


main()
