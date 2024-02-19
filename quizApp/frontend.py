from tkinter import *
from backend import Quiz


class QuizApp:
    
    def __init__(self, quiz):
        self.quiz = quiz

        self.win = Tk()
        self.win.title("Math Quiz")

        self.mainFrame = Frame(self.win)
        self.mainFrame.grid(row=0, column=0, padx=10, pady=10)

        self.newQuestion = StringVar()
        self.newAnswer = StringVar()
        self.newQuestion.set("Enter question here")
        self.newAnswer.set("Enter answer here")

        self.questionWidgets = []

    def run(self):
        self.createWidgets()
        self.win.mainloop()

    def createWidgets(self):
        self.deleteAllQuestionWidgets()

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
            column=3,
            padx=5,
            pady=5
        )

        numQuestions = self.quiz.getNumQuestions()

        for i in range(numQuestions):
            question = self.quiz.getQuestionAt(i)

            questionLabel = Label(
                self.mainFrame,
                text=question
            )
            questionLabel.grid(row=i+1, column=0)
            self.questionWidgets.append(questionLabel)

            self.userAnswer = Entry(
                self.mainFrame
            )
            self.userAnswer.grid(
                row=i+1,
                column=1,
                padx=5,
                pady=5
            )
            self.questionWidgets.append(self.userAnswer)

            checkAnswer = lambda index, userAnswer: self.checkAnswerAtIndex(index, userAnswer)

            checkAnswersButton = Button(
                self.mainFrame,
                text="Check",
                command=checkAnswer(i, self.questionWidgets[(i*2)-1])
            )
            checkAnswersButton.grid(
                row=i+1,
                column=2,
                padx=5,
                pady=5
            )

            removeQuestionButton = Button(
                self.mainFrame,
                text="Remove",
                command=lambda index=i: self.removeQuestion(index)
            )
            removeQuestionButton.grid(
                row=i+1,
                column=3,
                padx=5,
                pady=5
            )
            self.questionWidgets.append(removeQuestionButton)

    def addQuestion(self):
        question = self.newQuestion.get()
        answer = self.newAnswer.get()
        self.quiz.addQuestion(question, answer)

        self.newQuestion.set("Enter question here")
        self.newAnswer.set("Enter answer here")
        self.createWidgets()

    def removeQuestion(self, index):
        self.quiz.removeQuestionAt(index)
        self.createWidgets()

    def deleteAllQuestionWidgets(self):
        for widget in self.questionWidgets:
            widget.destroy()
        self.questionWidgets = []
    
    def checkAnswerAtIndex(self, index, userAnswer):
        if self.quiz.checkAnswerAt(index, userAnswer):
            self.userAnswer.configure(fg="green")
        else:
            self.userAnswer.configure(fg="red")


def main():
    quiz = Quiz()
    quiz.addQuestion("What's 2+2?", "4")
    quiz.addQuestion("What's 3*3?", "9")

    app = QuizApp(quiz)
    app.run()
main()