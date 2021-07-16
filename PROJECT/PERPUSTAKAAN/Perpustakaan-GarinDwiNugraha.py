def menu():
    print(' ______________________________________________________________________________ ')
    print('|                             LAYANAN PERPUSTAKAAN                             |')
    print('|                      Rumah Baca Komunitas Jendela Dunia                      |')
    print('|------------------------------------------------------------------------------|')
    print('|No|         Judul Buku              | Kategori | Kode Buku |  Biaya Sewa/hari |')
    print('|------------------------------------------------------------------------------|')
    print('| 1| A History Of Modern Indonesia   |          |    S01    |      Rp. 1000    |')
    print('| 2| Di Bawah Bendera Revolusi       |  SEJARAH |    S02    |      Rp. 1500    |')
    print('| 3| Catatan Seorang Demonstran      |          |    S03    |      Rp. 2000    |')
    print('| 4| Tetralogi Buru                  |  KODE: S |    S04    |      Rp. 1000    |')
    print('| 5| Aku Ingin Jadi Peluru           |          |    S05    |      Rp. 1500    |')
    print('|------------------------------------------------------------------------------|')
    print('| 6| 3 Jam Jago Ngoding              |          |    T01    |      Rp. 2000    |')
    print('| 7| Dasar Dasar Python              |  Bahasa  |    T02    |      Rp. 1500    |')
    print('| 8| Belajar C++ Sampai Mahir        |  Coding  |    T03    |      Rp. 1500    |')
    print('| 9| Aku Ingin Jadi Programer        |  Kode: T |    T04    |      Rp. 2000    |')
    print('|10| Buku Sakti HTML & JAVASCRIPT    |          |    T05    |      Rp. 1000    |')
    print('|------------------------------------------------------------------------------|')
    print('|11| Secret To Great Public Speaking |          |    L01    |      Rp. 2000    |')
    print('|12| Time Management                 |   Life   |    L02    |      Rp. 1500    |')
    print('|13| How To Master Your Habbits      |  Skills  |    L03    |      Rp. 2000    |')
    print('|14| Unlimited You                   |  Kode: L |    L04    |      Rp. 1000    |')
    print('|15| Bicara Itu Ada Seninya          |          |    L05    |      Rp. 1500    |')
    print('|------------------------------------------------------------------------------|')
    print('|Catatan: 1. Peminjam Harus Mengembalikan Buku Yang Di Pinjam Tepat Pada       |')
    print('|            Waktunya.                                                         |')
    print('|         2. Apabila Peminjam Telat Mengembalikan Buku, Maka Dikenakan         |')
    print('|            Biaya Denda Sebesar Rp 500/hari.                                  |')
    print('|______________________________________________________________________________|\n')
#bj = banyak judul, kb = kode buku, jb = judul buku, bb = banyak buku, hs = harga sewa,
# ts = total sewa, ws = waktu sewa
kb = []
jb = []
bb = []
hs = []
ts = []
i = 0
jum = 0
pilihan = 'y'
while (pilihan=='y'):
    print('\n')
    menu()
    print('Menu:')
    print(' ____________________')
    print('| 1. Pinjam Buku     |')
    print('| 2. Kembalikan Buku |')
    print('|____________________|')
    kode = input('Masukan Kode [1/2]: ')
    if kode == '1':
        print('\nInput Tanggal Pinjam')
        import datetime
        year1 = int(input('Masukan Tahun  : '))
        month1 = int(input('Masukan Bulan  : '))
        day1 = int(input('Masukan Tanggal: '))
        tgl1 = datetime.date(year1, month1, day1)
        print('\nInput Biodata Peminjam Buku Perpustakaan')
        nama = input('Nama Peminjam                    : ')
        nohp = input('Nomor Handphone                  : ')
        bj = int(input('Banyak Judul Yang Ingin Di Pinjam: '))
        ws = int(input('Waktu Sewa                       : '))
        while i < bj:
            print('\nBuku ke -', i + 1)
            kb.append(input('Kode Buku [S01/S02/S03/S04/S05/T01/T02/T03/T04/T05/L01/L02/L03/L04/L05]: '))
            bb.append(int(input('Banyak Buku: ')))
            if kb[i] == 'S01' or kb[i] == 's01':
                jb.append('A History Of Modern Indonesia  ')
                hs.append(1000)
                ts.append(ws * bb[i] * hs[i])
            elif kb[i] == 'S02' or kb[i] == 's02':
                jb.append('Di Bawah Bendera Revolusi      ')
                hs.append(1500)
                ts.append(ws * bb[i] * hs[i])
            elif kb[i] == 'S03' or kb[i] == 's03':
                jb.append('Catatan Seorang Demonstran     ')
                hs.append(2000)
                ts.append(ws * bb[i] * hs[i])
            elif kb[i] == 'S04' or kb[i] == 's04':
                jb.append('Tetralogi Buru                 ')
                hs.append(1000)
                ts.append(ws * bb[i] * hs[i])
            elif kb[i] == 'S05' or kb[i] == 's05':
                jb.append('Aku Ingin Jadi Peluru          ')
                hs.append(1500)
                ts.append(ws * bb[i] * hs[i])
            elif kb[i] == 'T01' or kb[i] == 't01':
                jb.append('3 Jam Jago Ngoding             ')
                hs.append(2000)
                ts.append(ws * bb[i] * hs[i])
            elif kb[i] == 'T02' or kb[i] == 't02':
                jb.append('Dasar Dasar Python             ')
                hs.append(1500)
                ts.append(ws * bb[i] * hs[i])
            elif kb[i] == 'T03' or kb[i] == 't03':
                jb.append('Belajar C++ Sampai Mahir       ')
                hs.append(1500)
                ts.append(ws * bb[i] * hs[i])
            elif kb[i] == 'T04' or kb[i] == 't04':
                jb.append('Aku Ingin Jadi Programer       ')
                hs.append(2000)
                ts.append(ws * bb[i] * hs[i])
            elif kb[i] == 'T05' or kb[i] == 't05':
                jb.append('Buku Sakti HTML & JAVASCRIPT   ')
                hs.append(1000)
                ts.append(ws * bb[i] * hs[i])
            elif kb[i] == 'L01' or kb[i] == 'l01':
                jb.append('Secret To Great Public Speaking')
                hs.append(2000)
                ts.append(ws * bb[i] * hs[i])
            elif kb[i] == 'L02' or kb[i] == 'l02':
                jb.append('Time Management                ')
                hs.append(1500)
                ts.append(ws * bb[i] * hs[i])
            elif kb[i] == 'L03' or kb[i] == 'l03':
                jb.append('How To Master Your Habbits     ')
                hs.append(2000)
                ts.append(ws * bb[i] * hs[i])
            elif kb[i] == 'L04' or kb[i] == 'l04':
                jb.append('Unlimited You                  ')
                hs.append(1000)
                ts.append(ws * bb[i] * hs[i])
            elif kb[i] == 'L05' or kb[i] == 'l05':
                jb.append('Bicara Itu Ada Seninya         ')
                hs.append(1500)
                ts.append(ws * bb[i] * hs[i])
            else:
                jb.append('Kode Yang Anda Input Salah     ')
                hs.append(0)
                ts.append(ws * bb[i] * hs[i])
            i = i + 1
        jh = 0
        b=0
        jum = 0
        print('')
        print('Berikut daftar rincian buku-buku yang anda pinjam selama', ws, 'hari:')
        while b < bj:
            jum = jum + bb[b]
            jh = jh + ts[b]
            print('%i | %i %s %s %s %i %s %i' % (b+1, bb[b], 'buku', jb[b], 'x', hs[b], '=', ts[b]))
            b = b+1
        print('--------------------------------------------------------- +')
        print('Total Biaya Sewa:                                Rp.', jh)
        print('\nTotal Buku Yang Anda Pinjam Sebanyak', jum, 'buku')
        print('Pembayaran Dilakukan Ketika Proses Pengembalian\n')
    elif kode == '2':
        cek = input('Masukan nama      : ')
        if cek == nama:
            print('\nAnda Meminjam Buku Pada', tgl1, 'selama', ws, 'hari')
            import datetime
            print('\nInput Tanggal Pengembalian Buku')
            year2 = int(input('Masukan Tahun  : '))
            month2 = int(input('Masukan Bulan  : '))
            day2 = int(input('Masukan Tanggal: '))
            tgl2 = datetime.date(year2, month2,day2)
            selisih = tgl2 - tgl1
            a = selisih.days
            if a > ws:
                den = (a-ws)*500
                print('\nPERINGATAN!!!')
                print('~ Anda Melebihi Batas Waktu Pinjam yaitu', a - ws, 'hari')
                print('~ Denda yang anda dapatkan sebesar 500 x', a-ws, 'hari =', den, 'Rupiah/buku')
                print('~ Karna anda meminjam', jum, 'buku, maka denda yang anda dapatkan yaitu:')
                print( jum, 'x', den, '=', jum*den, 'Rupiah')
            else:
                print('Anda Tidak Mendapat Denda')
                den = 0
            if cek == nama:
                print('\nStruk pembayaran yang anda dapatkan adalah:')
                print(' ______________________________________________________________________________ ')
                print('|                             LAYANAN PERPUSTAKAAN                             |')
                print('|                      Rumah Baca Komunitas Jendela Dunia                      |')
                print('|------------------------------------------------------------------------------|')
                print(' Biodata Peminjam: ', nama, '|', nohp, '|')
                print('|------------------------------------------------------------------------------|')
                print('|No| Judul Buku                      Banyak Buku     Harga Sewa   Total Sewa   |')
                print('|------------------------------------------------------------------------------|')
                jh = 0
                b = 0
                while b < bj:
                    jh = (jh) + ts[b]
                    print("| %i| %s   %i              %i           %i" % (b + 1, jb[b], bb[b], hs[b], ts[b]))
                    b = b + 1
                print('|  | Biaya Denda                                                    ', jum*den)
                print(' ----------------------------------------------------------------------------+')
                print('                                             Total Biaya Sewa  : Rp.', jh+(jum*den))
                bayar=int(input('                                             Masukan Uang Bayar: Rp. '))
                print('                                             Uang Kembali      : Rp.', bayar-(jh+(jum*den)))
        else:
            print('\n ~ Anda Tidak Meminjam Buku ~')
    pilihan = input('Apakah Anda Ingin Mengulang Kembali (y/n)?')
else:
    print('                       ----------------------------------------- ')
    print('                      |  ~    TERIMAKASIH SUDAH BERKUNJUNG    ~ |')
    print('                      |  ~ RUMAH BACA KOMUNITAS JENDELA DUNIA ~ |')
    print('                       ----------------------------------------- ')