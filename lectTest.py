from tkinter import *


class CoffeeShop:
    def __init__(self):
        self.customers = []

    def addCustomer(self, name):
        self.customers.append(name)

    def removeCustomerAt(self, index):
        del self.customers[index]

    def getCustomerAt(self, index):
        return self.customers[index]

    def getNumCustomers(self):
        return len(self.customers)


class CoffeeShopApp:
    def __init__(self, coffeeShop):
        self.coffeeShop = coffeeShop

        self.win = Tk()
        self.win.title("Coffee Shop")

        self.mainFrame = Frame(self.win)
        self.mainFrame.grid(
            row=0,
            column=0,
        )

        self.newCustomerName = StringVar()

    def run(self):
        self.createWidgets()
        self.win.mainloop()

    def createWidgets(self):
        customerEntry = Entry(
            self.mainFrame,
            textvariable=self.newCustomerName
        )
        customerEntry.grid(
            row=0,
            column=0,
        )

        addCustomerButton = Button(
            self.mainFrame,
            text="Add",
            command=self.addCustomer
        )
        addCustomerButton.grid(
            row=0,
            column=1,
        )

        numCustomers = self.coffeeShop.getNumCustomers()
        for i in range(numCustomers):
            customer = self.coffeeShop.getCustomerAt(i)
            customerLabel = Label(
                self.mainFrame,
                text=customer
            )
            customerLabel.grid(
                row=i+1,
                column=0,
            )

    def addCustomer(self):
        name = self.newCustomerName.get()
        self.coffeeShop.addCustomer(name)
        self.createWidgets()


def main():
    coffeeShop = CoffeeShop()

    coffeeShop.addCustomer("Alice")
    coffeeShop.addCustomer("Bob")
    coffeeShop.addCustomer("Charlie")

    app = CoffeeShopApp(coffeeShop)
    app.run()


main()
