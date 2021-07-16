apple_price = 2
# Berikan 10 ke variable money 
money = 10
#deklarasi variable money dengan nilai 10

input_count = input('Mau berapa apel?: ')
#input suatu nilai,yang mana nilai disimpan di variable input_count

count = int(input_count)
#variabel count mengambil data input_count dan merubahnya menjadi integer

total_price = apple_price * count
#total_price menerima nilai dari hasil apple_price dikali count
#count disini berarti jumlah apel yang diinginkan
#apple_price berarti harga apel


# Tambahkan control flow berdasarkan perbandingan antara money dan total_price
if money > total_price:
    #jika uang lebih besar dari harga total
    print("Anda telah membeli "+str(count)+" apel")
    #maka anda telah membeli "sekian" apel
    print("Uang Anda tinggal "+str(money-total_price))
    #dan uang anda sisa uang-harga total

elif money == total_price:
    #selain itu jika  uang sama dengan harga total
    print("Anda telah membeli "+str(count)+" apel")
    #anda telah membeli "sekian" apel
    print("Dompet Anda kosong")
    #dompetnya kosong
    
else:
    #selain itu semua
    print("Uang Anda tidak mencukupi")
    #uang tidak cukup
    print("Anda tidak dapat membeli apel sebanyak itu")
    #anda tidak bisa membeli apel sebanyak itu