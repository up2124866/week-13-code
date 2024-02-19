class CoffeeShop:
    
    def __init__(self, customerLimit):
        self.customerLimit = customerLimit
        self.customers = []

    def addCustomer(self, name):
        if len(self.customers) < self.customerLimit:
            self.customers.append(name)

    def removeCustomerAt(self, index):
        del self.customers[index]

    def getCustomerAt(self, index):
        return self.customers[index]

    def getNumCustomers(self):
        return len(self.customers)
    
    def getCustomerLimit(self):
        return self.customerLimit
