nim = ['2','3','1','0','3','1','0','2','3']
#nim2 ='231031023'
print(nim[1:3])
#print(nim2[1:3])

#akses item
print(f'item indeks 0:{nim[0]}')
print(f'item indeks 4:{nim[4]}')
print(f'item indeks terakhir:{nim[len(nim)-1]}')

#akses indeks negatif
print(f'item indeks terakhir: {nim[-1]}')
print(f'item indeks pertama: {nim[-len(nim)]}')
print(f'item indeks 6 [-3]: {nim[-3]}')
print(f'item indeks 4 [-5]: {nim[-5]}')
print(f'item indeks 7 [-2]: {nim[-2]}')

#akses indeks batas
print(f'item indeks 1,2,...:\n {nim[1:]}')
print(f'item indeks 3,4,...:\n {nim[3:]}')
print(f'item indeks 0,1,2:\n {nim[:3]}')
print(f'item indeks 0,1,2,3:\n {nim[:4]}')
print(f'item indeks semua:\n {nim[:]}')
print(f'item indeks [:8]:\n {nim[:-1]}')
print(f'item indeks [:6]:\n{nim[:-3]}')

#pengirisan
print(f'item indeks 1,2 : \n {nim[1:3]}')
print(f'item indeks 2,3,4: \n {nim[2:5]}')
print(f'item indeks kosong: \n {nim[3:3]}')
print(f'item indeks [8:8] kosong \n {nim[-1:-1]}')
print(f'item indeks [1:8]: \n {nim[1:-1]}')
print(f'item indeks [2:7: \n {nim[2:-2]}')

#latihan list
data = ['Afiqah',2023,'Aktif']
nilai= [90,89,93,97]

print('Nama: '+ data [0])
print('angkatan:', data[1])
print('status:'+ data[2])
print()

print(f'{data[0]} Status Kuliah\t: {data[2]}')
print(f'Data terbesar nilai adalah\t: {max(nilai)}')
print(f'Data terkecil nilai adalah\t: {min(nilai)}')
print(f'Data terbesr nilai adalah\t: {sum(nilai)/len(nilai)}')

#latihan tuple
data = ('Afiqah',2023,'Aktif')
nilai= (90,89,93,97)

print('data[1]')
print('data[-1]')
print('nilai[1:-1]')
print()

print(f'Jumlah nilai {data[0]} adalah: {len(nilai)}')
print(f'Data terbesar nilai adalah\t: {max(nilai)}')
print(f'Data terkecil nilai adalah\t: {min(nilai)}')
print(f'Data terbesar nilai adalah\t: {sum(nilai)/len(nilai)}')

#Latihan Nested List
data = [('Afiqah',2023,'Aktif'),
        (90,89,93,97),
        (20,22),
        ('S1-Reguler','Ganjil')]
 
print(data[0][0])
print(data[-1][0])
print(data[2][0:])
print()

print(f'Program pendidikan {data[0][0]}\t: {data[3][0]}')
print(f'Angkatan\t: {data[0][1]}-{data[3][1]}')
print(f'Jumlah Nilai {data[0][0]} Adalah\t: {len(data[1])}')
print(f'Data terbesar nilai {data[0][0]} Adalah\t: {max(nilai)}')
print(f'Data terbesar nilai {data[0][0]} Adalah\t: {min(nilai)}')
print(f'Data terbesar nilai {data[0][0]} Adalah\t: {sum(nilai)/len(nilai)}')

#Tugas 4 
data = [['Afiqah',2023,'Aktif'],
[90,89,93,97],
[20,22],
['S1-Reguler','Ganjil']]
matkul = ['Agama Islam','Pancasila','Bahasa Indonesia','Wawasan Cinta IPTEK dan IMTAQ']
sks    = [2,2,2,2]
# Menambahkan matkul dan sks ke dalam data (di akhir)
data.append(matkul)
data.append(sks)
# Mata kuliah 1: Matkul1 dengan jumlah 2 sks
print(f'Matkul1 :{data[4][0]} dengan jumlah {data[-1][0]}sks\n')
# Mata kuliah 2: Matkul2 dengan jumlah 2 sks
print(f'Matkul2 :{data[4][1]} dengan jumlah {data[-1][1]}sks\n')
# Mata kuliah 3: Matkul3 dengan jumlah 2 sks
print(f'Matkul3 :{data[4][2]} dengan jumlah {data[-1][2]}sks\n')
# Mata kuliah 4: Matkul4 dengan jumlah 2 sks
print(f'Matkul4 :{data[4][3]} dengan jumlah {data[-1][3]}sks\n')
data[4].append('Pengantar Pemrograman')
data[5].append(3)
# Tambahkan 3 matkul dengan sks nya
data[4].append('Pengantar Teknologi Informasi')
data[5].append(3)
data[4].append('Kalkulus Dasar I')

data[5].append(3)
data[4].append('Sains Terpadu')
data[5].append(3)
# Mata kuliah 5: Matkul5 dengan jumlah .. sks
print(f'Matkul5 :{data[4][4]} dengan jumlah {data[-1][4]}sks\n')
# Mata kuliah 6: Matkul6 dengan jumlah .. sks
print(f'Matkul6 :{data[4][5]} dengan jumlah {data[-1][5]}sks\n')
# Mata kuliah 7: Matkul7 dengan jumlah .. sks
print(f'Matkul7 :{data[4][6]} dengan jumlah {data[-1][6]}sks\n')
# Mata kuliah 8: Matkul8 dengan jumlah .. sks
print(f'Matkul8 :{data[4][7]} dengan jumlah {data[-1][7]}sks\n')
print(data[0][0])
print(data[-1][0])
print(data[2][0:])
print(f'Nama Mahasiswa {data[0][0]} dengan NIM {"".join(nim)}')
print(f'Program pendidikan {data[0][0]}: {data[3][0]}')
print(f'Angkatan : {data[0][1]}-{data[3][1]}')
print(f'Jumlah nilai {data[0][0]} adalah: {len(data[1])}')
print(f'Data terbesar {data[0][0]} adalah: {max(data[1])}')
print(f'Data terkecil {data[0][0]} adalah: {min(data[1])}')
print(f'Rata-rata nilai {data[0][0]} adalah: {sum(data[1])/len(data[1])}')