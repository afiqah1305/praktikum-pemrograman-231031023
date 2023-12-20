while True:
    pilih = input('Pilihan : ')
    if pilih == 'ya' or pilih == 'tidak':
        if pilih.lower() == 'ya':
            print('selamat datang')
        elif pilih.lower() == 'tidak':
            print('sampai jumpa')
        break


"""
1.) "while True" Ini adalah loop yang akan terus berjalan selama kondisinya adalah True. Karena kondisinya selalu True, maka loop ini akan berjalan terus-menerus sampai ada break yang menghentikannya.

2.) "pilih = input('Pilihan : ')" Mengambil input dari pengguna dan menyimpannya dalam variabel pilih.

3.) "if pilih == 'ya' or pilih == 'tidak'" Memeriksa apakah input pengguna adalah 'ya' atau 'tidak'. Jika ya, maka program akan masuk ke dalam blok if.

4.) "if pilih.lower() == 'ya'" Jika input pengguna adalah 'ya' (dalam huruf apa pun), program akan masuk ke dalam blok ini dan mencetak 'selamat datang'.

5.) "elif pilih.lower() == 'tidak'" Jika input pengguna adalah 'tidak' (dalam huruf apa pun), program akan masuk ke dalam blok ini dan mencetak 'sampai jumpa'.

6.) "break" Setelah mencetak pesan, pernyataan break digunakan untuk menghentikan loop. Dengan demikian, program akan keluar dari loop dan berakhir.

"""
