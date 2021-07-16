class ATMcard:
    def __init__(self,defaultPin,defaultBalance):
        self.defaultPin = defaultPin #Pin itu nomor Pin
        self.defaultBalance = defaultBalance #Balance itu saldo

    def defaultCek(self):
        #Mengapa tidak menggunakan defaultPin,dikarenakan
        #self.defaultPin sudah digunakan sebagai pengembalian,
        #jadi defaultPin hanya sebagai pengisi nilai untuk mengisi
        #variabel utama (variabel self.defaultPin)
        return self.defaultPin

    def defaultBalanceCek(self):
        #Mengapa tidak menggunakan defaultBalance,dikarenakan
        #self.defaultBalance sudah digunakan sebagai pengembalian,
        #jadi defaultBalance hanya sebagai pengisi nilai untuk mengisi
        #variabel utama (variabel self.defaultBalance)
        return self.defaultBalance


    