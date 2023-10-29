from tkinter import *


class MathQuiz:
    def __init__(self):
        self.questions = []
        self.answers = []

    def addQuestion(self, question, answer):
        self.questions.append(question)
        self.answers.append(answer)

    def getQuestionAt(self, index):
        return self.questions[index]

    def getAnswerAt(self, index):
        return self.answers[index]

    def getNumQuestions(self):
        return len(self.questions)

    def removeQuestionAt(self, index):
        del self.questions[index]
        del self.answers[index]


class MathQuizApp:
    def __init__(self, mathQuiz):
        self.mathQuiz = mathQuiz

        self.root = Tk()
        self.root.title("Math Quiz")

        self.mainFrame = Frame(self.root)
        self.mainFrame.grid(row=0, column=0)

        self.newQuestion = StringVar()
        self.newAnswer = StringVar()

        self.questionWidgets = []

    def run(self):
        self.createWidgets()
        self.root.mainloop()

    def createWidgets(self):
        self.deleteAllQuestionWidgets()

        questionEntry = Entry(self.mainFrame, textvariable=self.newQuestion)
        questionEntry.grid(row=0, column=0)

        answerEntry = Entry(self.mainFrame, textvariable=self.newAnswer)
        answerEntry.grid(row=0, column=1)

        addQuestionButton = Button(self.mainFrame, text="Add Question", command=self.addQuestion)
        addQuestionButton.grid(row=0, column=2)

        numQuestions = self.mathQuiz.getNumQuestions()
        for i in range(numQuestions):
            question = self.mathQuiz.getQuestionAt(i)
            questionLabel = Label(self.mainFrame, text=question)
            questionLabel.grid(row=i+1, column=0)
            self.questionWidgets.append(questionLabel)

            studentAnswer = Entry(self.mainFrame)
            studentAnswer.grid(row=i+1, column=1)
            self.questionWidgets.append(studentAnswer)

            checkButton = Button(
                self.mainFrame,
                text="Check",
                command=lambda i=i, studentAnswer=studentAnswer: self.checkAnswer(i, studentAnswer)
            )
            checkButton.grid(row=i+1, column=2)
            self.questionWidgets.append(checkButton)

            removeQuestionButton = Button(
                self.mainFrame,
                text="Remove",
                command=lambda index=i: self.removeQuestion(index)
            )
            removeQuestionButton.grid(row=i+1, column=3)
            self.questionWidgets.append(removeQuestionButton)

    def addQuestion(self):
        question = self.newQuestion.get()
        answer = self.newAnswer.get()
        self.mathQuiz.addQuestion(question, answer)
        self.createWidgets()

    def checkAnswer(self, index, studentAnswer):
        correctAnswer = self.mathQuiz.getAnswerAt(index)
        if studentAnswer.get() == correctAnswer:
            print("Correct!")
        else:
            print("Incorrect!")

    def removeQuestion(self, index):
        self.mathQuiz.removeQuestionAt(index)
        self.createWidgets()

    def deleteAllQuestionWidgets(self):
        for widget in self.questionWidgets:
            widget.destroy()


def main():
    quiz = MathQuiz()
    quiz.addQuestion("What's 2+2?", "4")
    quiz.addQuestion("What's 3*3?", "9")

    app = MathQuizApp(quiz)
    app.run()


main()
