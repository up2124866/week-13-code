from tkinter import *


class PosApp:
    def __init__(self):
        self.win = Tk()
        self.win.title("POS System")

        self.total = DoubleVar()
        self.total.set(0.00)

        self.newItemPrice = DoubleVar()

    def run(self):
        self.createWidgets()
        self.win.mainloop()

    def createWidgets(self):
        totalLabel = Label(
            self.win,
            text=f"Total Bill: £{self.total.get():.2f}"
        )
        totalLabel.pack()

        addItemButton = Button(
            self.win,
            text="Add Item",
            command=lambda: self.createNewWin(totalLabel)
        )
        addItemButton.pack()

    def createNewWin(self, totalLabel):
        newWin = Toplevel(self.win)
        newWin.title("Add Item to Bill")

        itemPriceLabel = Label(newWin, text="Item Price (£):")
        itemPriceLabel.pack()

        itemPriceEntry = Entry(
            newWin,
            textvariable=self.newItemPrice
        )
        itemPriceEntry.pack()

        addButton = Button(
            newWin,
            text="Add to Bill",
            command=lambda: self.updateBill(
                totalLabel, newWin)
        )
        addButton.pack()

    def updateBill(self, totalLabel, newWin):
        newTotal = self.total.get() + self.newItemPrice.get()
        self.total.set(newTotal) # Update the total (this does not update the label)
        self.newItemPrice.set(0.00) # Reset the entry box for the new item
        totalLabel.config(
            text=f"Total Bill: £{self.total.get():.2f}")
        # Without the config line, the totalLabel will not update

        newWin.destroy()


def main():
    app = PosApp()
    app.run()


main()
