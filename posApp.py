from tkinter import *


class PosApp:
    def __init__(self):
        self.mainWindow = Tk()
        self.mainWindow.title("POS System")

        self.total = DoubleVar()
        self.total.set(0.00)

        self.newItemPrice = DoubleVar()

    def run(self):
        self.createWidgets()
        self.mainWindow.mainloop()

    def createWidgets(self):
        totalLabel = Label(
            self.mainWindow,
            text=f"Total Bill: £{self.total.get():.2f}"
        )
        totalLabel.pack()

        addItemButton = Button(
            self.mainWindow,
            text="Add Item",
            command=lambda: self.createNewWindow(totalLabel)
        )
        addItemButton.pack()

    def createNewWindow(self, totalLabel):
        newWindow = Toplevel(self.mainWindow)
        newWindow.title("Add Item to Bill")

        itemPriceLabel = Label(newWindow, text="Item Price (£):")
        itemPriceLabel.pack()

        itemPriceEntry = Entry(
            newWindow,
            textvariable=self.newItemPrice
        )
        itemPriceEntry.pack()

        addButton = Button(
            newWindow,
            text="Add to Bill",
            command=lambda: self.updateBill(
                totalLabel, newWindow)
        )
        addButton.pack()

    def updateBill(self, totalLabel, newWindow):
        newTotal = self.total.get() + self.newItemPrice.get()
        self.total.set(newTotal) # Update the total (this does not update the label)
        self.newItemPrice.set(0.00) # Reset the entry box for the new item
        totalLabel.config(
            text=f"Total Bill: £{self.total.get():.2f}")
        # Without the config line, the totalLabel will not update

        newWindow.destroy()


def main():
    app = PosApp()
    app.run()


main()
