from tkinter import *


class CoffeeShopApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Coffee Shop")

        self.mainFrame = Frame(self.root)
        self.mainFrame.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
        )

        self.newCustomerName = StringVar()
    
    def run(self):
        self.createWidgets()
        self.root.mainloop()

    def createWidgets(self):
        customerEntry = Entry(
            self.mainFrame,
            textvariable=self.newCustomerName
        )
        customerEntry.grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
        )

        addCustomerButton = Button(
            self.mainFrame,
            text="Add",
            command=self.addCustomer
        )
        addCustomerButton.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
        )

    def addCustomer(self):
        name = self.newCustomerName.get()
        # Do something with name (e.g., display it in a label)
        self.newCustomerName.set("")

        customerLabel = Label(
            self.mainFrame,
            text=name
        )
        customerLabel.grid(
            row=1,
            column=0,
            columnspan=2,
            padx=5,
            pady=5,
        )


def main():
    app = CoffeeShopApp()
    app.run()


main()
