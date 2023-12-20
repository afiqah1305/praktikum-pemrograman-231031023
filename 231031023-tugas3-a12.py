pw_benar = "ab2222354"
percobaan = 3
a = True
while a:
    masukan = input("masukkan password: ")
    if masukan == pw_benar:
        print("selamat anda login!")
        a = False
    else: 
        if percobaan == 0: 
            print("Anda dibanned!")
            a = False
        else:
            print("password yang anda masukkan salah! coba lagi")
            print(f'percobaan anda sisa {percobaan} kali')
            percobaan -= 1
