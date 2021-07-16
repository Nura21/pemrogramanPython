def pemilihan_data(pilihan):
if pilihan == "1":
        import KARYAWAN as KARYAWAN2
        KARYAWAN2.tampilkan_judul()
elif pilihan == "2":
        import PERUSAHAAN as PERUSAHAAN2
        PERUSAHAAN2.pemrosesan_data()
elif pilihan =="3" :
        import DATA_KARYAWAN as DATA_KARYAWAN2
        DATA_KARYAWAN2
else :
        print("Ada Kesalahan Pemilihan !!!!")
return pilihan

perulangan="y"

while(perulangan=="y"):    
pilihan=input("\nMasukkan pilihan 1. Karyawan 2. Perusahaan 3. Data Karyawan : ")
pemilihan_data(pilihan)
perulangan=input("\nApa anda ingin mengulang(y/n) : ")