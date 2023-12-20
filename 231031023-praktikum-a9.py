def judul():
    print('PROGRAM MENGHITUNG LUAS DAN KELILING'.center(30))
    print('BANGUN DATAR PERSEGI'.center(35))
    print()

def inputan():
    panjang = float(input('Masukkan Panjang: '))
    lebar = float(input('Masukkan Lebar: '))
    return panjang,lebar

def luasan(panjang,lebar):
    hasil = panjang * lebar
    return hasil

def keliling(panjang,lebar):
    hasil = (panjang+lebar)*2
    return hasil 

def tampil(pesan,nilai):
    print(f'Hasil Perhitungan nilai {pesan}: {nilai}')

def pilihan():
    pilih = input('Apakah Ingin Melanjutkan? [y/n]')
    if pilih =='y':
        a = True
    else:
        a=False
        print('Sampai Jumpa.')    


a =True
while a:
    # Judul
    judul()
    panjang,lebar =inputan()

    # inputan panjang dan lebar
    panjang,lebar = inputan()

    # hitung luas
    luas = luasan(panjang,lebar)

    # hitung keliling
    kel = keliling(panjang,lebar)

    # cetak atau display
    tampil('luas',luas)
    tampil('keliling',kel)

    pilih = input('Apakah Ingin Melanjutkan? [y/n]: ')
    if pilih == 'y':
        a = True
    else:
        a = False
        print('Sampai Jumpaaaaa.')
