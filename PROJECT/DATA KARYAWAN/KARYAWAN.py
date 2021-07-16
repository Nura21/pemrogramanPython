def tampilkan_judul():
    print("\t\t\tSelamat datang di SISTEM PENDAPATAN")
    masukkan_data_karyawan()
        
def masukkan_data_karyawan():
   print("=================================") 
   nama=input("Masukkan nama karyawan : ") 
   print("\n1. Manajer") 
   print("\n2. Akuntan")
   print("\n3. Marketing")
   print("\n4. Staff") 
   print("\n5. Pegawai")
   jabatan=input("\nMasukkan jabatan : ")
   print("\n=================================")
   olahdata(nama,jabatan)   

def olahdata(nama,jabatan):
    if jabatan == "1":
        gaji_karyawan=20000000
        pendapatan=potong_pajak(gaji_karyawan)
        print("=================================")
        print("\n|Nama Karyawan : "+nama+"  |")
        print("\n|Gaji Karyawan : Rp"+str(gaji_karyawan)+"       |")
        print("\n|Gaji Bersih   : Rp"+str(pendapatan)+"      |")
        print("=================================")    
    elif jabatan == "2":
        gaji_karyawan=10000000
        pendapatan=potong_pajak(gaji_karyawan)
        print("=================================")
        print("\n|Nama Karyawan : "+nama+"  |")
        print("\n|Gaji Karyawan : Rp"+str(gaji_karyawan)+"       |")
        print("\n|Gaji Bersih   : Rp"+str(pendapatan)+"      |")
        print("=================================")
    elif jabatan == "3":
        gaji_karyawan=15000000
        pendapatan=potong_pajak(gaji_karyawan)
        print("=================================")
        print("\n|Nama Karyawan : "+nama+"  |")
        print("\n|Gaji Karyawan : Rp"+str(gaji_karyawan)+"       |")
        print("\n|Gaji Bersih   : Rp"+str(pendapatan)+"      |")
        print("=================================")
    elif jabatan == "4":
        gaji_karyawan=8000000
        pendapatan=potong_pajak(gaji_karyawan)
        print("=================================")
        print("\n|Nama Karyawan : "+nama+"  |")
        print("\n|Gaji Karyawan : Rp"+str(gaji_karyawan)+"       |")
        print("\n|Gaji Bersih   : Rp"+str(pendapatan)+"      |")
        print("=================================")
    elif jabatan == "5":
        gaji_karyawan=5000000
        pendapatan=potong_pajak(gaji_karyawan)
        print("=================================")
        print("\n|Nama Karyawan : "+nama+"  |")
        print("\n|Gaji Karyawan : Rp"+str(gaji_karyawan)+"       |")
        print("\n|Gaji Bersih   : Rp"+str(pendapatan)+"      |")
        print("=================================")
        print("hai")    
    else :
        print("Ada Kesalahan data Karyawan!!!!")

def potong_pajak(pendapatan):
    #x=10/100
    
    pendapatan-=(pendapatan*10)/100
    return pendapatan