print("=================================================")
print("Data Karyawan".center(50))
print("=================================================")

a = input("Nama : ")
b = input("ID Karyawan : ")

if a=="Bima" and b=="10001":
    print("Tempat Tinggal : Cibeusi"+"\nJabatan : Manajer"+"\nGaji : Rp20000000")
elif a=="Basu" and b=="10002":
    print("Tempat Tinggal : Sayang"+"\nJabatan : Akuntan"+"\nGaji : Rp10000000")
elif a=="Dewo" and b=="10003":
    print("Tempat Tinggal : Cileunyi"+"\nJabatan : Marketing"+"\nGaji : Rp15000000")
elif a=="Irfan" and b=="10004":
    print("Tempat Tinggal : Hegarmanah"+"\nJabatan : Staff"+"\nGaji : Rp8000000")
elif a=="Ujang" and b=="10005":
    print("Tempat Tinggal : Ciseke"+"\nJabatan : Pegawai"+"\nGaji : Rp5000000")
else:
    print("Data Karyawan Tidak Tersedia")