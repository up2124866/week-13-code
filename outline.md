# Outline
## **Chapter 1: Dynamically updating the frontend of an app based on its backend**
1. **Recap of Basic Concepts**
    - Brief overview of Tkinter and event-driven programming
    - A revisit of `Button`, `Label`, `Entry`, and their respective properties.
    - Quick review of basic event handlers and the `command` parameter.
  
2. **Creating backends for GUI apps and updating the frontend using the backend**
    - Introducing backend classes for existing apps:
        - CoffeeShop class for the coffee shop queue management app (the lecture slides).
        - Question and Quiz class for the quiz app (the worksheet).
    - Passing the backend to the frontend and using it to update the frontend.
        - Populating the queue with customers in the coffee shop app.
        - Populating the quiz with questions in the quiz app.
        - Passing the instance of the backend class to the frontend class.
        - Iterating over the data in the backend class to populate the frontend.
        - Calling the backend class methods to update the data in the backend and the frontend (e.g., adding a customer to the queue in the coffee shop app and adding a question to the quiz in the quiz app).

## **Chapter 2: Passing parameters to event handlers using lambdas with default parameters**
1. **Why do we need to pass parameters to event handlers? Why can't we just use the `command` parameter?**
    - The `command` parameter doesn't allow us to pass parameters to event handlers.
    - We need to pass parameters to event handlers to update the model and the view.

2. **Introduction to `lambda` function, examples and its use cases**
    - What is `lambda`? Let's look at some examples. How we can convert a function to a lambda.
    - Why do we need it in this context?

3. **Functions and `lambda` function with default parameters**
    - What are default parameters?
    - How to define functions with default parameters.
    - Why do we need default parameters in this context? How we can use lambdas with default parameters to pass parameters to event handlers. 

4. **Passing parameters to event handlers using lambdas with default parameters**
    - Updating the backend using lambdas with default parameters in the frontend.
        - Removing a customer in the coffee shop app.
        - Removing a question in the quiz app and checking the answer of a question.

## **Chapter 3: Apps can have multiple windows**
1. **Why do we need multiple windows?**
    - Applications can have multiple windows to show different information to the user, separate different functionalities, etc.
    - Examples of apps that need multiple windows:
        - A login window and a main window.
        - A main window and a settings window.

2. **Creating a new window (TopLevel)**
    - Introduction to `Toplevel` and its significance.
    - Passing values from the main window (`Tk`) to the new window (`Toplevel`).
    - Passing values from the new window (`Toplevel`) to the main window (`Tk`).
    - Closing the new window (`Toplevel`).
