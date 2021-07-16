#Di file ini,file dipergunakan hanya sebagai penyedia fungsi

def validate(hand):
    if hand < 0 or hand > 2:
        #jika angka kurang dari 0 atau lebih dari 2 maka akan false pengembaliannya
        return False
    return True

def print_hand(hand, name='Tamu'):
    #lemparan data dari file script.py dengan pemanggilan fungsi print hand
    # menerima hand dan name

    hands = ['Batu', 'Kertas', 'Gunting']
    #adanya deklarasi list 

    print(name + ' memilih: ' + hands[hand])
    #hand dipakai sebagai index disini

def judge(player, computer):
    if player == computer:
        return 'Seri'
    elif player == 0 and computer == 1:
        return 'Kalah'
    elif player == 1 and computer == 2:
        return 'Kalah'
    elif player == 2 and computer == 0:
        return 'Kalah'
    else:
        return 'Menang'
#coba coba
#hahahaha = 9
