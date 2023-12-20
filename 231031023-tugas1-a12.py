a = True
perulangan = 0
while a:
    if perulangan>=5:
        print('program selesai')
        a = False
    else:
         perulangan +=1
    print(f'Menjalankan Program Sebanyak{perulangan}kali')

 # Inisial variabel a sebagai True untuk mengawali perulangan
    a = True

 # Inisial variabel perulangan sebagai center untuk jumlah perulangan
    perulangan = 0

    # Memulai loop while yang akan terus berjalan selama variabel a bernilai True
    while a:
        # Memriksa apakah jumlah perulangan sudah lebih dari atau sama dengan 5
        if perulangan>=5:
            # Jika sudah mencapai 5 kali perulangan, cetak pesan dan ubah nilai a menjadi False untuk menghentikan loop
            print('program selesai')
            a = False
        else:
                # Jika belum mencapai 5 kali perulangan, tambahkan counter perulangan dan cetak pesan
                perulangan += 1
                print(f'Menjalankan program sebanyak {perulangan} kali')
