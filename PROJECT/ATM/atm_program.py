import random
import datetime
from customer import Customer


atm = Customer(id)

#looping pemeriksaan
while True:
    id = int(input("Masukkan pin anda : "))
    percobaan = 0

    while(id !=int(atm.custPinCek()) and percobaan < 3):
        id =int(input("Masukkan pin anda,dan ulangi lagi : "))
        percobaan += 1
        if percobaan == 3:
            print("Error. Silahkan ambil kartu dan coba lagi. .")
            exit()

    print("\nSelamat datang")
    print("\nMenu Utama :")
    print("\n1. Cek saldo")
    print("\n2. Debet")
    print("\n3. Simpan")
    print("\n4. Ganti pin")
    print("\n5.Keluar")

    pilihanMenu=int(input("\nPilihan menu : "))
    if pilihanMenu == 1:
        print("\n Saldo sekarang : "+ str(atm.custBalanceCek()) + "\n")
    elif pilihanMenu == 2:
        nominal_saldo = float(input("Masukkan nominal saldo : "))
        verifikasi_nominal_saldo = input("Konfirmasi : Akan melakukan debet sebesar " + str(nominal_saldo) + " :")
        
        if verifikasi_nominal_saldo == "y":
            print("Saldo awal : " + str(atm.custBalanceCek()))
        else:
            break

        if nominal < atm.custBalanceCek():
            atm.debet(nominal_saldo)
            print("Transaksi berhasil!")
            print("Saldo sisa : " + str(atm.custBalanceCek()))
        
        else:
            print("Maaf,saldo tidak cukup")
            print("Silahkan lakukan penambahan nominal saldo")
    elif pilihanMenu == 3:
        nominal_saldo = float(input("Masukkan nominal saldo : "))
        verifikasi_deposit = input("Konfirmasi: Anda akan melakukan penyimpanan nominal : " + str(nominal_saldo) + " :")

        if verifikasi_deposit == "y":
            atm.simpan(nominal_saldo)
            print("Saldo anda : " + str(atm.custBalanceCek()) + "\n")
        else:
            break
    elif pilihanMenu == 4:
        verifikasi_pin = int(input("Masukkan pin anda : "))

        while verifikasi_pin != int(atm.custPinCek()):
            print("Pin salah,silahkan masukkan pin : ")
        
        perubahan_pin = int(input("Silahkan masukkan pin baru : "))
        print("Pin anda berhasil diganti !")

        verifikasi_pinBaru = int(input("Masukkan pin baru : "))

        if verifikasi_pinBaru == perubahan_pin:
            print("Pin baru anda berhasil !")
        else:
            print("Maaf,pin salah") 
    elif pilihanMenu == 5:
        print("Resi tercetak otomatis \n" + "\nHarap simpan tanda teria ini \n sebagai bukti transaksi")
        print("No Rekord : ",random.randint(10000,100000))
        print("Tanggal : " + str(datetime.datetime.now()))
        print("Saldo akhir : " + str(atm.custBalanceCek()))
        print("Terimakasih telah menggunakan ATM Progate!")
        exit()
    else:
        print("Error. Maaf,menu tidak tersedia")