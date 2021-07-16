from atm_card import ATMcard

class Customer(ATMcard):
    def __init__(self,id,custPin=1234,custBalance=10000):
        self.id = id
        self.custPin = custPin
        self.custBalance = custBalance
    
    def idCek(self):
        return self.id
    
    def custPinCek(self):
        return self.custPin
    
    def custBalanceCek(self):
        return self.custBalance

    def debet(self,nominal):
        self.custBalance -= nominal

    def simpan(self,nominal):
        self.custBalance += nominal