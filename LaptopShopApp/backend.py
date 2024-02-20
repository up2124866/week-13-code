class Laptop:

    ramOptions = {
        4: 0,
        8: 50,
        16: 100,
        32: 200
    }

    def __init__(self, brand, basePrice):
        self.brand = brand
        self.basePrice = basePrice
        self.ram = 4

    def getBrand(self):
        return self.brand

    def getRam(self):
        return self.ram

    def getPrice(self):
        ramPrice = self.ramOptions[self.ram]
        return self.basePrice + ramPrice

    def setRam(self, ram):
        if ram in self.ramOptions:
            self.ram = ram

    def __str__(self):
        output = f"{self.brand} Laptop with {self.ram} GB RAM "
        output += f"priced at £{self.getPrice()}"
        return output



class GamingLaptop(Laptop):

    gpuOptions = {
        "NVIDIA GTX 1650": 0,
        "NVIDIA RTX 3070": 250,
        "NVIDIA RTX 4080": 350,
        "AMD RX 6800M": 280
    }

    def __init__(self, brand, basePrice):
        super().__init__(brand, basePrice)
        self.gpu = "NVIDIA GTX 1650"

    def getGpu(self):
        return self.gpu

    def setGpu(self, gpu):
        if gpu in self.gpuOptions:
            self.gpu = gpu

    def getPrice(self):
        gpuPrice = self.gpuOptions[self.gpu]
        return super().getPrice() + gpuPrice

    def __str__(self):
        output = f"{self.brand} Laptop with {self.ram} GB RAM "
        output += f"and {self.gpu} priced at £{self.getPrice()}"
        return output



class ShoppingCart:

    def __init__(self):
        self.laptops = []
        self.total = 0

    def addLaptop(self, laptop):
        self.laptops.append(laptop)

    def getLaptops(self):
        return self.laptops

    def getTotal(self):
        self.total = 0
        for laptop in self.laptops:
            self.total += laptop.getPrice()
        return abs(self.total)
    
    def removeLaptopAtIndex(self, index):
        self.total -= self.laptops[index].getPrice()
        self.laptops.remove(self.laptops[index])

    def __str__(self):
        output = "Shopping cart contains:\n"
        for laptop in self.laptops:
            output += f"{laptop}\n"
        output += f"Total price is £{self.total}"
        return output

def testLaptop():
    laptop = Laptop("Dell", 999.99)
    print("laptop's brand is", laptop.getBrand())
    print("laptop's RAM is", laptop.getRam())
    print("laptop's price is", laptop.getPrice())  # 999.99

    laptop.setRam(32)
    print("laptop's RAM is now", laptop.getRam())
    laptop.setRam(30)
    print("laptop's RAM is still", laptop.getRam())

    print("laptop's price is now", laptop.getPrice())  # 999.99 + 200 = 1199.99

    print(laptop)


def testShoppingCart():
    cart = ShoppingCart()
    dellLaptop = Laptop("Dell", 999.99)
    appleLaptop = Laptop("Apple", 1349.00)
    msiLaptop = GamingLaptop("MSI", 1599.00)
    msiLaptop.setRam(16)
    msiLaptop.setGpu("AMD RX 6800M0")
    cart.addLaptop(dellLaptop)
    cart.addLaptop(appleLaptop)
    cart.addLaptop(msiLaptop)

    print("Shopping cart contains:")
    for laptop in cart.getLaptops():
        print(laptop)
    print(f"Total price is £{cart.getTotal()}")

    print(cart)


def testGamingLaptop():
    gamingLaptop = GamingLaptop("Razer", 2399.99)
    print("Gaming laptop's brand is", gamingLaptop.getBrand())
    print("Gaming laptop's price is", gamingLaptop.getPrice())
    print("Gaming laptop's ram is", gamingLaptop.getRam())
    print("Gaming laptop's GPU is", gamingLaptop.getGpu())

    gamingLaptop.setGpu("NVIDIA RTX 3070")
    print("Gaming laptop's GPU is now", gamingLaptop.getGpu())
    print("Gaming laptop's price is now", gamingLaptop.getPrice())

    print(gamingLaptop)