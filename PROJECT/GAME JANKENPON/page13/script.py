import utils
#import module utils

# import module random
import random

#kegunaan import adalah sebagai perantara,
#dimana kita bisa mengetik sesuatu yang berhubungan dengan kode file yang terpisah

print('Memulai permainan Batu Kertas Gunting!')
player_name = input('Masukkan nama Anda: ')
#player_name sebagai variabel penerima nama


print('Pilih tangan: (0: Batu, 1: Kertas, 2: Gunting)')
player_hand = int(input('Masukkan nomor (0-2): '))
#variabel player_hand

if utils.validate(player_hand):
#kenapa menggunakan utils. , kenapa tidak langsung validate saja?
#jika tidak menggunakan utils. akan error,karena jika ingin terbaca hingga ke antar file
#harus menggunakan utils.
    
    #coba coba
    #print(str(utils.hahahaha))
    #sama halnya dengan variabel biasa,harus menggunakan utils

    computer_hand = random.randint(0,2)
    # Tetapkan nomor acak antara 0 dan 2 ke computer_hand menggunakan random.randint
    
    utils.print_hand(player_hand, player_name)
    #disini berarti pemanggilan fungsi untuk fungsi print_hand,dengan parameter
    #player_hand,player hand digunakan sebagai jenis tangan yang digunakan untuk suit

    utils.print_hand(computer_hand, 'Komputer')
    #disini berarti pemanggilan fungsi untuk fungsi print_hand,dengan parameter
    #computer_hand,computer hand digunakan sebagai jenis tangan yang digunakan untuk suit
    
    result = utils.judge(player_hand, computer_hand)
    #memanggil fungsi judge dengan utils.judge
    #pemanggilan suatu fungsi dengan menggunakan nama file utils yang berada di file lain
    #hanya berlaku bila berbeda class atau tidak memiliki class atau tidak satu class
    print('Hasil: ' + result)
else:
    print('Mohon masukkan nomor yang benar')
