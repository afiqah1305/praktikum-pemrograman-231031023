max_attempts = 3
pw1 = '123A'
pw2 = '456B'
pw3 = '789C'

while True:
    if max_attempts != 0:
        try:
            inp = (input('Silahkan masukkan password 1: '))
            if inp == pw1:
                print('Berhasil')
                inp = (input('Silahkan masukkan password 2: '))
                if inp == pw2:
                    print('Berhasil')
                    inp = (input('Silahkan masukkan password 3: '))
                    if inp == pw3:
                        print('Anda berhasil login')
                        break
                    elif inp != pw3:
                        max_attempts -= 1
                        print('Password salah.')
                        print(f'Kesempatan anda tersisa {max_attempts} kali!')
                        continue
                    else:
                        print('Anda terblokir. Silahkan coba lain kali!')
                        break
                elif inp != pw2:
                    max_attempts -= 1
                    print('Password salah.')
                    print(f'Kesempatan anda tersisa {max_attempts} kali!')
                    continue
                else:
                    print('Anda terblokir. Silahkan coba lain kali!')
                    break
            elif inp != pw1:
                max_attempts -= 1
                print('Password salah.')
                print(f'Kesempatan anda tersisa {max_attempts} kali')
                continue

        except ValueError:
            print('Mohon masukkan format dengan benar!')
            max_attempts -= 1
            print(f'Anda memiliki {max_attempts} kesempatan tersisa!\n')
    else:
        print('Anda terblokir. Kesempatan anda telah habis')
        break