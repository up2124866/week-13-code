from tkinter import *


class SettingsWindow:
    def __init__(self):
        self.win = Tk()
        self.win.title("Main Window")
        self.win.geometry("100x100")

        self.mainFrame = Frame(self.win)
        self.mainFrame.pack()

        self.widgets = []

    def run(self):
        self.createWidgets(12)
        self.win.mainloop()

    def createWidgets(self, fontSize):
        self.destroyWidgets()

        helloLabel = Label(
            self.mainFrame,
            text="Hello World",
            font=("Arial", fontSize),
        )
        helloLabel.pack()
        self.widgets.append(helloLabel)

        byeLabel = Label(
            self.mainFrame,
            text="Goodbye Mars",
            font=("Arial", fontSize),
        )
        byeLabel.pack()
        self.widgets.append(byeLabel)

        settingsButton = Button(
            self.mainFrame,
            text="Change settings",
            command=lambda: self.changeSettings(fontSize)
        )
        settingsButton.pack()
        self.widgets.append(settingsButton)

    def changeSettings(self, currentFontSize):
        fontSize = StringVar()
        fontSize.set(currentFontSize)

        settingsWindow = Toplevel(self.win)
        settingsWindow.title("Change settings")

        settingsFrame = Frame(settingsWindow)
        settingsFrame.pack()

        fontSizeLabel = Label(
            settingsFrame,
            text="Font size"
        )
        fontSizeLabel.pack()

        fontSizeEntry = Entry(
            settingsFrame,
            textvariable=fontSize
        )
        fontSizeEntry.pack()

        saveButton = Button(
            settingsFrame,
            text="Save",
            command=lambda: self.saveSettings(
                settingsWindow=settingsWindow,
                fontSize=fontSize.get()
            )
        )
        saveButton.pack()

    def saveSettings(self, settingsWindow, fontSize):
        settingsWindow.destroy()
        self.createWidgets(fontSize)
        # Update the size of the main window appropriately
        self.win.geometry(f"{fontSize*10}x100")

    def destroyWidgets(self):
        for widget in self.widgets:
            widget.destroy()
        self.widgets = []


def main():
    settingsWindow = SettingsWindow()
    settingsWindow.run()


main()
