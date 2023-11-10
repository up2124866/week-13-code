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
            command=lambda: self.createNewWin(numberLabel)
        )
        updateButton.pack()

    def createNewWin(self, numberLabel):
        newWin = Toplevel(self.win)
        newWin.title("Update number")

        newNumEntry = Entry(
            newWin,
            textvariable=self.num
        )
        newNumEntry.pack()

        newNumButton = Button(
            newWin,
            text="Update number",
            command=lambda: self.updateNum(numberLabel, newWin)
        )
        newNumButton.pack()

    def updateNum(self, numberLabel, newWin):
        numberLabel.config(text=f"Number: {self.num.get()}")
        newWin.destroy()


def main():
    app = App()
    app.run()


main()
