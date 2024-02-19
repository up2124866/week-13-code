class Recipe:

    def __init__(self, recipeTitle: str, recipeCookTime: int, recipeCookingSteps: str):
        self.recipeTitle = recipeTitle
        self.recipeCookTime = recipeCookTime
        self.recipeCookingSteps = recipeCookingSteps

    def getRecipeTitle(self):
        return self.recipeTitle
    
    def getRecipeCookTime(self):
        return self.recipeCookTime
    
    def getRecipeCookingSteps(self):
        return self.recipeCookingSteps
    


class RecipeBook:

    def __init__(self):
        self.recipeList = []

    def addRecipe(self, newRecipe):
        self.recipeList.append(newRecipe)

    def getRecipeAtIndex(self, index):
        return self.recipeList[index]
    
    def getNumOfRecipe(self):
        return len(self.recipeList)