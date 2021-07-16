#cara yang baik dalam mengimport
from menu_item import MenuItem

#cara pendeklarasian oop
menu_item1 = MenuItem('Roti Lapis', 5)
#masuk ke constructor
menu_item2 = MenuItem('Kue Coklat', 4)
menu_item3 = MenuItem('Kopi', 3)
menu_item4 = MenuItem('Jus Jeruk', 2)

menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]#object dimasukkan ke dalam array
#cuman di python,object bisa dimasukkan ke dalam array

index = 0
#penanda

for menu_item in menu_items:
    #anggap aja menu_item itu kaya i untuk membantu pengulangan
    print(str(index) + '. ' + menu_item.info())
    #index sebagai penanda angka 1 2 3 
    #menu_item.info() -> ini berarti menu_item1.info() menu_item2.info()
    #kemudian masuk ke fungsi yang ada file menu_item.py di dalam class MenuItem
    #sebelum masuk ke fungsi info,masuknya ke constructor dulu
    
    index += 1 # increment

print('--------------------')

order = int(input('Masukkan nomor menu: '))
selected_menu = menu_items[order]
print('Item yang di pilih: ' + selected_menu.name)

# Terima input dari console, dan Berikan input ke variable count
count = int(input("Jumlah pesanan (diskon 10% untuk 3 atau lebih): "))

# Panggil method get_total_price 
result = selected_menu.get_total_price(count)

# Cetak 'Total harga adalah $____'
print("Total harga adalah $" + str(result))
