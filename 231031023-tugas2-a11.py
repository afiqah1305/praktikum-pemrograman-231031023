#latihan 2

inp = input ('masukan suatu input: ')
if len(inp) != 3:
    print('panjang string', len (inp),'tidak sama dengan 3')
else :
    print('panjang input sesuai yang di inginkan')
nilai = int(input('masukan nilai: '))
if nilai >= 90:
    print('Nilai huruf: A')
elif nilai > 75:
    print('Nilai huruf: B')
elif nilai > 55:
    print('Nilai huruf: C')
else:
    print('Nilai huruf: D')
