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

        self.root = Tk()
        self.root.title("Coffee Shop")

        self.mainFrame = Frame(self.root)
        self.mainFrame.grid(
            row=0,
            column=0,
        )

        self.newCustomerName = StringVar()

        self.customerWidgets = []

    def run(self):
        self.createWidgets()
        self.root.mainloop()

    def createWidgets(self):
        self.deleteAllWidgets()

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
            text="Add Customer",
            command=self.addCustomer
        )
        addCustomerButton.grid(
            row=0,
            column=1,
        )

        numberOfCustomers = self.coffeeShop.getNumCustomers()
        for i in range(numberOfCustomers):
            customer = self.coffeeShop.getCustomerAt(i)
            customerLabel = Label(
                self.mainFrame,
                text=customer
            )
            customerLabel.grid(
                row=i+1,
                column=0,
            )
            self.customerWidgets.append(customerLabel)

            removeCustomerButton = Button(
                self.mainFrame,
                text="Remove",
                command=lambda index=i: self.removeCustomer(index)
            )
            removeCustomerButton.grid(
                row=i+1,
                column=1,
            )
            self.customerWidgets.append(removeCustomerButton)

    def addCustomer(self):
        name = self.newCustomerName.get()
        self.coffeeShop.addCustomer(name)
        self.createWidgets()

    def removeCustomer(self, index):
        self.coffeeShop.removeCustomerAt(index)
        self.createWidgets()

    def deleteAllWidgets(self):
        for widget in self.customerWidgets:
            widget.destroy()
        # Alternatively, we could do this:
        # for widget in self.mainFrame.winfo_children():
        #     widget.destroy()


def main():
    coffeeShop = CoffeeShop()

    coffeeShop.addCustomer("Alice")
    coffeeShop.addCustomer("Bob")
    coffeeShop.addCustomer("Charlie")

    app = CoffeeShopApp(coffeeShop)
    app.run()


main()
