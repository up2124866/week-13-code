from tkinter import *


class QuizApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Math Quiz")

        self.mainFrame = Frame(self.root)
        self.mainFrame.grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        self.newQuestion = StringVar()
        self.newAnswer = StringVar()
        self.newQuestion.set("Enter question here")
        self.newAnswer.set("Enter answer here")

    def run(self):
        self.createWidgets()
        self.root.mainloop()

    def createWidgets(self):
        questionEntry = Entry(
            self.mainFrame,
            textvariable=self.newQuestion,
            width=20
        )
        questionEntry.grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        answerEntry = Entry(
            self.mainFrame,
            textvariable=self.newAnswer,
            width=20
        )
        answerEntry.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        addQuestionButton = Button(
            self.mainFrame,
            text="Add",
            command=self.addQuestion
        )
        addQuestionButton.grid(
            row=0,
            column=2,
            padx=5,
            pady=5
        )

    def addQuestion(self):
        question = self.newQuestion.get()

        questionLabel = Label(
            self.mainFrame,
            text=question
        )
        questionLabel.grid(
            row=1,
            column=0,
            padx=5,
            pady=5
        )

        answerEntry = Entry(
            self.mainFrame,
            width=20,
        )
        answerEntry.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )


def main():
    app = QuizApp()
    app.run()


main()
