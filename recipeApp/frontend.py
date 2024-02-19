from backend import *
from tkinter import *

class RecipeBookApp:

    def __init__(self, recipeBook):
        self.recipeBook = recipeBook

        self.win = Tk()
        self.win.title("Recipe Book App")

        self.mainframe = Frame(self.win)
        self.mainframe.grid(
            padx=5,
            pady=5
        )

    def createWidgets(self):
        for i in range(self.recipeBook.getNumOfRecipe()):

            recipeTitleLabel = Label(
                self.mainframe,
                text=self.recipeBook.getRecipeAtIndex(i).getRecipeTitle(),
                width=20
            )
            recipeTitleLabel.grid(
                column=0,
                row=i,
                padx=5,
                pady=5
            )


            recipeCookTimeLabel = Label(
                self.mainframe,
                text=f"{self.recipeBook.getRecipeAtIndex(i).getRecipeCookTime()} mins"
            )
            recipeCookTimeLabel.grid(
                column=1,
                row=i,
                padx=5,
                pady=5
            )


            recipeViewButton = Button(
                self.mainframe,
                text="View Recipe",
                command=lambda index=i: self.viewRecipe(index)
            )
            recipeViewButton.grid(
                column=2,
                row=i,
                padx=5,
                pady=5
            )
    def viewRecipe(self, index):
        self.newWin = Toplevel(
            self.win,
            padx=5,
            pady=5
        )
        self.newWin.grid()

        recipeTitle = Label(
            self.newWin,
            text=self.recipeBook.getRecipeAtIndex(index).getRecipeTitle()
        )
        recipeTitle.grid()

        cookTimeLabel = Label(
            self.newWin,
            text=f"Cook time: {self.recipeBook.getRecipeAtIndex(index).getRecipeCookTime()} minutes"
        )
        cookTimeLabel.grid()

        stepText = Text(
            self.newWin,
            height=10,
            width=40)
        stepText.grid()
        stepText.insert('1.0', chars=self.splitTextIntoSteps(index))
        stepText.configure(state="disabled")

    def splitTextIntoSteps(self, index):
        output = ""
        recipeSteps = (self.recipeBook.getRecipeAtIndex(index).getRecipeCookingSteps())
        for i, steps in enumerate(recipeSteps.split(', ')):
            output += f"Step {i+1}: {steps}.\n"
        return output


    def run(self):
        self.createWidgets()
        self.win.mainloop()


myRecipe1 = Recipe("Spaghetti", 30, "poop in hands, look at hands, clap hands together, repeat")
myRecipe2 = Recipe("Chicken Curry", 45, "get in car, turn on car, drive to closest school, run over children, get arrested")
myRecipe3 = Recipe("Noodles", 15, "pick up phone, call 911, wait for police, get arrested")

myRecipeBook = RecipeBook()
myRecipeBook.addRecipe(myRecipe1)
myRecipeBook.addRecipe(myRecipe2)
myRecipeBook.addRecipe(myRecipe3)

myRecipeApp = RecipeBookApp(myRecipeBook)
myRecipeApp.run()