money = 20
#Deklarasi variabel money dengan nilai 20

items = {'apel': 2, 'pisang': 4, 'jeruk': 6}
#ada dictionary dengan index apel bernilai 2
# index pisang bernilai 4
# index jeruk bernilai 6

for item_name in items:
    #untuk item_name dengan range menyesuaikan dengan total items
    #jadi anggap item_name itu i,i akan terus bertambah sesuai dengan jumlah items
    #items berjumlah 3 index,maka dari itu , i akan berulang sebanyak 3 kali

    print('--------------------------------------------------')
    print('Anda memiliki ' + str(money) + ' dolar di dompet Anda')
    #money disini dalam penampilan wajib menggunakan str,karena memang jika ingin menampilkan suatu
    # data harus di konvert dulu ke string

    print('Harga setiap ' + item_name + ' ' + str(items[item_name]) + ' dolar')
    #item_name disini hanya sebagai i,namun perbedaannya tidak akan menampilkan angka 1 2 3,
    #melainkan akan menampilkan indexnya,diketahui bahwa index dalam items adalah apel pisang jeruk
    #mengapa bisa begitu? karena "for item_name in items" berarti,item_name merujuk kepada
    #dictionary items
    
    input_count = input('Mau berapa ' + item_name + '?:')
    #jumlah buah yang diinginkan

    print('Anda akan membeli ' + input_count + ' ' + item_name)
    #menampilkan output jumlah buah dan nama indexnya
        
    count = int(input_count)
    #konversian

    total_price = items[item_name] * count
    #total price di dapat dari nilai dari index dictionary items dikali jumlah buah yang sudah dikonversi

    print('Harga total adalah ' + str(total_price) + ' dolar')
    #output untuk harga total yang sudah dikonversi menggunakan str
    

    if money >= total_price:
        print('Anda telah membeli ' + input_count + ' ' + item_name)
        money -= total_price
        # Ketika money sama dengan 0, cetak 'Dompet Anda kosong' dan hentikan loop
        if money == 0:
            print("Dompet Anda kosong")
            break
        
        
    else:
        print('Uang Anda tidak mencukupi')
        print('Anda tidak dapat membeli ' + item_name + ' sebanyak itu')
# Menggunakan variable money dan tipe conversion, cetak 'Uang Anda tinggal ___ dolar'
print("Uang Anda tinggal " + str(money) + " dolar")
