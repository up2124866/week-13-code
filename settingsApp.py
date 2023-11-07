from tkinter import *


class SettingsWindow:
    def __init__(self):
        self.win = Tk()
        self.win.title("Main Window")
        self.win.geometry("100x100")

        self.mainFrame = Frame(self.win)
        self.mainFrame.pack()

        # self.fontColour = StringVar()
        # self.fontColour.set("black")

        self.fontSize = IntVar()
        self.fontSize.set(12)

        self.widgets = []

    def run(self):
        self.createWidgets()
        self.win.mainloop()

    def createWidgets(self):
        self.destroyWidgets()

        helloLabel = Label(
            self.mainFrame,
            text="Hello World",
            # fg=self.fontColour.get(),
            font=("Arial", self.fontSize.get()),
        )
        helloLabel.pack()
        self.widgets.append(helloLabel)

        byeLabel = Label(
            self.mainFrame,
            text="Goodbye Mars",
            # fg=self.fontColour.get(),
            font=("Arial", self.fontSize.get()),
        )
        byeLabel.pack()
        self.widgets.append(byeLabel)

        settingsButton = Button(
            self.mainFrame,
            text="Change settings",
            command=self.changeSettings
        )
        settingsButton.pack()
        self.widgets.append(settingsButton)

    def changeSettings(self):
        settingsWindow = Toplevel(self.win)
        settingsWindow.title("Change settings")

        settingsFrame = Frame(settingsWindow)
        settingsFrame.pack()

        # fontColourLabel = Label(
        #     settingsFrame,
        #     text="Font colour"
        # )
        # fontColourLabel.pack()

        # fontColourEntry = Entry(
        #     settingsFrame,
        #     textvariable=self.fontColour,
        # )
        # fontColourEntry.pack()

        fontSizeLabel = Label(
            settingsFrame,
            text="Font size"
        )
        fontSizeLabel.pack()

        fontSizeEntry = Entry(
            settingsFrame,
            textvariable=self.fontSize
        )
        fontSizeEntry.pack()

        saveButton = Button(
            settingsFrame,
            text="Save",
            command=lambda: self.saveSettings(settingsWindow)
        )
        saveButton.pack()

    def saveSettings(self, settingsWindow):
        settingsWindow.destroy()
        self.createWidgets()

    def destroyWidgets(self):
        for widget in self.widgets:
            widget.destroy()
        self.widgets = []


def main():
    settingsWindow = SettingsWindow()
    settingsWindow.run()


main()
