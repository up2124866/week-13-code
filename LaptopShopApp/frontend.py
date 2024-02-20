from backend import *
from tkinter import *

class LaptopShopApp:

    def __init__(self, shoppingCart):
        self.shoppingCart = shoppingCart

        self.win = Tk()
        self.win.title("Laptop Shop")

        self.mainframe = Frame(self.win)
        self.mainframe.grid()

        self.laptopType = StringVar()
        self.newLaptopBrand = StringVar()
        self.newLaptopPrice = StringVar()
        self.newLaptopRam = StringVar()
        self.newLaptopGpu = StringVar()
        self.newLaptopGpuSubmit = ""
        self.newLaptopTotalPrice = StringVar()
        self.laptopType.set("Laptop")
        self.newLaptopRam.set("4 GB")
        self.newLaptopGpu.set("NVIDIA GTX 1650: £0")

        self.widgets = []

    def createWidgets(self):
        self.deleteAllWidgets()
        cartLabel1 = Label(
            self.mainframe,
            text="Laptop"
        )
        cartLabel1.grid(column=0, row=0, padx=5, pady=5)

        cartLabel2 = Label(
            self.mainframe,
            text="RAM"
        )
        cartLabel2.grid(column=1, row=0, padx=5, pady=5)

        cartLabel3 = Label(
            self.mainframe,
            text="GPU"
        )
        cartLabel3.grid(column=2, row=0, padx=5, pady=5)

        cartLabel4 = Label(
            self.mainframe,
            text="Price"
        )
        cartLabel4.grid(column=3, row=0, padx=5, pady=5)



        i = 0

        for i in range(len(self.shoppingCart.getLaptops())):
            brandLabel = Label(
                self.mainframe,
                text=self.shoppingCart.getLaptops()[i].getBrand()
            )
            brandLabel.grid(
                column=0,
                row=i+1,
                padx=5,
                pady=5
            )
            self.widgets.append(brandLabel)

            ramLabel = Label(
                self.mainframe,
                text=f"{self.shoppingCart.getLaptops()[i].getRam()} GB"
            )
            ramLabel.grid(
                column=1,
                row=i+1,
                padx=5,
                pady=5
            )
            self.widgets.append(ramLabel)

            gpuLabel = Label(
                self.mainframe,
                text=self.getGpu(i)
            )
            gpuLabel.grid(
                column=2,
                row=i+1,
                padx=5,
                pady=5
            )
            self.widgets.append(gpuLabel)

            priceLabel = Label(
                self.mainframe,
                text=f"£{self.shoppingCart.getLaptops()[i].getPrice()}"
            )
            priceLabel.grid(
                column=3,
                row=i+1,
                padx=5,
                pady=5
            )
            self.widgets.append(priceLabel)

            editButton = Button(
                self.mainframe,
                text="Edit",
                command=lambda index=i: self.createEditWindow(index)
            )
            editButton.grid(
                column=4,
                row=i+1,
                padx=5,
                pady=5
            )
            self.widgets.append(editButton)

            deleteButton = Button(
                self.mainframe,
                text="Delete",
                command=lambda index=i: self.removeWidgetAtIndex(index)
            )
            deleteButton.grid(
                column=5,
                row=i+1,
                padx=5,
                pady=5
            )
            self.widgets.append(deleteButton)

        numberOfLaptopLabel = Label(
            self.mainframe,
            text=f"Laptops in cart: {len(self.shoppingCart.getLaptops())}"
        )
        numberOfLaptopLabel.grid(
            column=0,
            row=i+2,
            padx=5,
            pady=5
        )
        self.widgets.append(numberOfLaptopLabel)

        totalPriceLabel = Label(
            self.mainframe,
            text=f"Total Price: £{self.shoppingCart.getTotal():.2f}"
        )
        totalPriceLabel.grid(
            column=2,
            row=i+2,
            columnspan=2,
            padx=5,
            pady=5,
            sticky=E
        )
        self.widgets.append(totalPriceLabel)

        addLaptopButton = Button(
            self.mainframe,
            text="Add Laptop",
            command=self.createNewLaptopWindow
        )
        addLaptopButton.grid(
            column=4,
            row=i+2,
            padx=5,
            pady=5,
            columnspan=2
        )
        self.widgets.append(addLaptopButton)


    def createEditWidget(self, index):
        self.newMainframe = Toplevel(self.win)
        self.newMainframe.title("Edit Laptop")
        self.newMainframe.grid()

        self.selectedRam = StringVar()
        self.selectedRam.set(f"{self.shoppingCart.getLaptops()[index].getRam()} GB")
        self.selectedGpu = StringVar()
        self.selectedGpu.set(self.getGpu(index))

        self.priceWidget = []

        brandLabel = Label(
            self.newMainframe,
            text=self.shoppingCart.getLaptops()[index].getBrand()
        )
        brandLabel.grid(
            column=0,
            row=0,
            padx=5,
            pady=5
        )

        ramOption = OptionMenu(
            self.newMainframe,
            self.selectedRam,
            "4 GB: £0",
            "8 GB: £50",
            "16 GB: £100",
            "32 GB: £200",
            command=lambda _: self.setRamAtIndex(index)
        )
        ramOption.grid(
            column=1,
            row=0,
            padx=5,
            pady=5
        )

        if 'GamingLaptop' in f"{type(self.shoppingCart.getLaptops()[index])}":
            gpuOption = OptionMenu(
                self.newMainframe,
                self.selectedGpu,
                "NVIDIA GTX 1650: £0",
                "NVIDIA RTX 3070: £250",
                "NVIDIA RTX 4080: £350",
                "AMD RX 6800M: £280",
                command=lambda _: self.setGpuAtIndex(index)
            )
            gpuOption.grid(
                column=2,
                row=0,
                padx=5,
                pady=5
            )
        
        confirmButton = Button(
            self.newMainframe,
            text="Confirm Changes",
            command=self.confirmEdit
        )
        confirmButton.grid(
            column=4,
            row=0,
            padx=5,
            pady=5
        )

    def createEditWidgetPrice(self, index):
        priceLabel = Label(
            self.newMainframe,
            text=f"£{self.shoppingCart.getLaptops()[index].getPrice()}"
        )
        priceLabel.grid(
            column=3,
            row=0,
            padx=5,
            pady=5
        )
        self.priceWidget.append(priceLabel)



    
    def deleteAllWidgets(self):
        for widget in self.widgets:
            widget.destroy()
        self.widgets = []

    def createEditWindow(self, index):
        self.createEditWidget(index)
        self.createEditWidgetPrice(index)

    def createNewLaptopWindow(self):
        self.addNewLaptopWindow()
        self.createNewLaptopPriceWidget()

    def removeWidgetAtIndex(self, index):
        self.shoppingCart.removeLaptopAtIndex(index)
        self.createWidgets()

    def getGpu(self, index):
        if 'GamingLaptop' in f"{type(self.shoppingCart.getLaptops()[index])}":
            return self.shoppingCart.getLaptops()[index].getGpu()
        else:
            return 'N/A'
        
    def setRamAtIndex(self, index):
        self.shoppingCart.getLaptops()[index].setRam(int(self.selectedRam.get()[0:2]))
        self.priceWidget[0].destroy()
        self.priceWidget = []
        self.createEditWidgetPrice(index)
        
    def setGpuAtIndex(self, index):
        gpu = "empty"
        for gpuSplit in self.selectedGpu.get().split(":"):
            if "empty" in gpu:
                gpu = gpuSplit

        self.shoppingCart.getLaptops()[index].setGpu((gpu))
        self.priceWidget[0].destroy()
        self.priceWidget = []
        self.createEditWidgetPrice(index)

    def confirmEdit(self):
        self.newMainframe.destroy()
        self.createWidgets()

    def addNewLaptopWindow(self):
        self.newLaptopFrame = Toplevel(self.win)
        self.newLaptopFrame.grid()
        self.newLaptopFrame.title("Add Laptop")

        self.newLaptopWidget = []
        self.newLaptopPriceWidgetList = []

        laptopTypeLabel = Label(
            self.newLaptopFrame,
            text="Choose Which Laptop"
        )
        laptopTypeLabel.grid(
            column=0,
            row=0,
            padx=5,
            pady=5
        )
        self.newLaptopWidget.append(laptopTypeLabel)

        laptopTypeOption = OptionMenu(
            self.newLaptopFrame,
            self.laptopType,
            "Laptop",
            "Gaming Laptop",
            command=lambda _: self.chosenLaptopType()
        )
        laptopTypeOption.grid(
            column=1,
            row=0,
            padx=5,
            pady=5
        )
        self.newLaptopWidget.append(laptopTypeOption)

        laptopBrandLabel = Label(
            self.newLaptopFrame,
            text="Laptop Brand: "
        )
        laptopBrandLabel.grid(
            column=0,
            row=1,
            padx=5,
            pady=5
        )
        self.newLaptopWidget.append(laptopBrandLabel)

        laptopBrandEntry = Entry(
            self.newLaptopFrame,
            textvariable=self.newLaptopBrand
        )
        laptopBrandEntry.grid(
            column=1,
            row=1,
            padx=5,
            pady=5
        )
        self.newLaptopWidget.append(laptopBrandEntry)

        laptopBasePriceLabel = Label(
            self.newLaptopFrame,
            text="Base Price: "
        )
        laptopBasePriceLabel.grid(
            column=0,
            row=2,
            padx=5,
            pady=5
        )
        self.newLaptopWidget.append(laptopBasePriceLabel)

        laptopBasePriceEntry = Entry(
            self.newLaptopFrame,
            textvariable=self.newLaptopPrice
        )
        laptopBasePriceEntry.grid(
            column=1,
            row=2,
            padx=5,
            pady=5
        )
        self.newLaptopPrice.trace_add("write", self.updateTotalPrice)
        self.newLaptopWidget.append(laptopBasePriceEntry)

        ramLabel = Label(
            self.newLaptopFrame,
            text="RAM: "
        )
        ramLabel.grid(
            column=0,
            row=3,
            padx=5,
            pady=5
        )
        self.newLaptopWidget.append(ramLabel)

        ramOption = OptionMenu(
            self.newLaptopFrame,
            self.newLaptopRam,
            "4 GB: £0",
            "8 GB: £50",
            "16 GB: £100",
            "32 GB: £200",
            command=lambda _: self.createNewLaptopPriceWidget()
        )
        ramOption.grid(
            column=1,
            row=3,
            padx=5,
            pady=5
        )
        self.newLaptopWidget.append(ramOption)


    def createNewLaptopPriceWidget(self):
        self.deletePriceWidget()
        priceLabel = Label(
            self.newLaptopFrame,
            text=f"Laptop Price: £{self.getNewLaptopPrice() + Laptop.ramOptions[int(self.newLaptopRam.get()[0:2])] + self.getNewGpuPrice()}"
        )
        priceLabel.grid(
            column=0,
            row=5,
            padx=5,
            pady=5,
            columnspan=2
        )
        self.newLaptopPriceWidgetList.append(priceLabel)
        self.newLaptopWidget.append(priceLabel)

        submitButton = Button(
            self.newLaptopFrame,
            text="Add to cart",
            command=self.addToCart
        )
        submitButton.grid(
            column=0,
            row=6,
            padx=5,
            pady=5,
            columnspan=2
        )
        self.newLaptopPriceWidgetList.append(submitButton)
        self.newLaptopWidget.append(submitButton)


    def addToCart(self):
        if self.laptopType.get() == "Gaming Laptop":
            newLaptop = GamingLaptop(self.newLaptopBrand.get(), self.getNewLaptopPrice())
            newLaptop.setRam(int(self.newLaptopRam.get()[0:2]))
            newLaptop.setGpu(self.newLaptopGpuSubmit)
        else:
            newLaptop = Laptop(self.newLaptopBrand.get(), self.getNewLaptopPrice())
            newLaptop.setRam(int(self.newLaptopRam.get()[0:2]))
        self.shoppingCart.addLaptop(newLaptop)
        self.newLaptopFrame.destroy()
        self.createWidgets()

    def getNewLaptopPrice(self):
        try:
            return float(self.newLaptopPrice.get())
        except ValueError:
            return 0

    def getNewGpuPrice(self):
        try:
            return GamingLaptop.gpuOptions[self.newLaptopGpuSubmit]
        except KeyError:
            return 0

    def chosenLaptopType(self):
        if self.laptopType.get() == "Gaming Laptop":
            self.gpuLabel = Label(
                self.newLaptopFrame,
                text="GPU: "
            )
            self.gpuLabel.grid(
                column=0,
                row=4,
                padx=5,
                pady=5
            )
            self.newLaptopWidget.append(self.gpuLabel)

            self.newGpuOption = OptionMenu(
                self.newLaptopFrame,
                self.newLaptopGpu,
                "NVIDIA GTX 1650: £0",
                "NVIDIA RTX 3070: £250",
                "NVIDIA RTX 4080: £350",
                "AMD RX 6800M: £280",
                command=lambda _: self.setGpuForNewLaptop()
            )
            self.newGpuOption.grid(
                column=1,
                row=4,
                padx=5,
                pady=5
            )
            self.newLaptopWidget.append(self.newGpuOption)
        else:
            try:
                self.gpuLabel.destroy()
                self.newGpuOption.destroy()
            except AttributeError:
                pass

    def deleteAllNewWindowWidgets(self):
        for widget in self.newLaptopWidget:
            widget.destroy()
        self.newLaptopWidget = []

    def setGpuForNewLaptop(self):
        gpuSplit = []
        for graphicsCard in self.newLaptopGpu.get().split(":"):
            gpuSplit.append(graphicsCard)

        self.newLaptopGpuSubmit = gpuSplit[0]
        self.createNewLaptopPriceWidget()

    def updateTotalPrice(self, *args):
        self.createNewLaptopPriceWidget()

    def deletePriceWidget(self):
        for widget in self.newLaptopPriceWidgetList:
            widget.destroy()
        self.newLaptopPriceWidgetList = []




    def run(self):
        self.createWidgets()
        self.win.mainloop()


def main():
    cart = ShoppingCart()
    dellLaptop = Laptop("Dell", 999.99)
    appleLaptop = Laptop("Apple", 1349.00)
    msiLaptop = GamingLaptop("MSI", 1599.00)
    msiLaptop.setRam(16)
    msiLaptop.setGpu("AMD RX 6800M0")
    cart.addLaptop(dellLaptop)
    cart.addLaptop(appleLaptop)
    cart.addLaptop(msiLaptop)
    myApp = LaptopShopApp(cart)
    myApp.run()
main()