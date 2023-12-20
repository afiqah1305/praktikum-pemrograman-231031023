#Fungsi Rekursif Fibonacci
def fibonacci(n):
    if n < 0:
        print('Tidak ada bilangan yang bernilai negatif')
    elif n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#Program utama
input_nilai = int(input("Masukkan sebuah bilangan: "))
hasil = fibonacci(input_nilai)
print('Fibonacci (%d) = %d' % (input_nilai,hasil))