from tkinter import *


class App:

    def __init__(self):
        self.win = Tk()
        self.win.title("Main Window")

        self.mainFrame = Frame(self.win)
        self.mainFrame.pack(padx=10, pady=10)

        self.num = IntVar()
        self.num.set(12)

    def run(self):
        self.createWidgets()
        self.win.mainloop()

    def createWidgets(self):
        numberLabel = Label(
            self.mainFrame,
            text=f"Number: {self.num.get()}"
        )
        numberLabel.pack(padx=5, pady=5)

        updateButton = Button(
            self.mainFrame,
            text="Update number",
            command=lambda: self.createNewWin(numberLabel)
        )
        updateButton.pack(padx=5, pady=5)

    def createNewWin(self, numberLabel):
        newWin = Toplevel(self.win)
        newWin.title("Update number")

        newWinFrame = Frame(newWin)
        newWinFrame.pack(padx=10, pady=10)

        newNumEntry = Entry(
            newWinFrame,
            textvariable=self.num
        )
        newNumEntry.pack(padx=5, pady=5)

        newNumButton = Button(
            newWinFrame,
            text="Update number",
            command=lambda: self.updateNum(numberLabel, newWin)
        )
        newNumButton.pack(padx=5, pady=5)

    def updateNum(self, numberLabel, newWin):
        numberLabel.config(text=f"Number: {self.num.get()}")
        self.num.set(0)
        newWin.destroy()


def main():
    app = App()
    app.run()
