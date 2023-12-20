#Fungsi Rekursif factorial dengan perulangan
def faktorial(nilai):
    if nilai <= 1:
        return 1
    else:
        return nilai * faktorial(nilai-1)

#Program Utama
input_nilai=int(input('masukkan nilai: '))
for i in range(input_nilai + 1):
    print('%2d ! = %d' % (i,faktorial(i)))