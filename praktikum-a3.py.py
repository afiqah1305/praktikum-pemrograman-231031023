print('Tugas Praktikum 3'.center(40))
nama = '\Afiqah '
nim  = '231031023'
prodi= 'Sistem Informasi A'
print(f'''
Nama\t: {nama}
NIM\t: {nim}
prodi\t: {prodi}''')

'''Dari beberapa string berikut, buatkan manipulasi kode
agar hasil outpunya sesuai'''
print('\n'*2)


print('----------STR1---------')
str1 = 'duFort Frankel Von Neumann'
a = str1.upper()
a = a.split()
print(a[-1],a[0],a[1],a[2])
#output: NEUMANN DUFORT FRANKEL VON

print()

print('----------STR2---------')
str2 = 'duFort Frankel Von Neumann'
a = str2.upper()
a = a.split()
print(a[0][0]+a[1][0]+a[2][0],a[-1])
#output: DFV NEUMANN

print()

print('----------STR3---------')
str3 = 'duFort Frankel Von Neumann'
a = str3.upper()
a = a.split()
print(a[0],a[1][0],a[2][0],a[-1][0])
#output: DUFORT F V N

print()

print('----------STR4---------')
str4 = 'duFOrt Frankel Von Neumann'
a = str4.upper()
a = a.split()
print(a[-1][-1].upper(),a[0][0:2].lower()+a[0][2:3]+a[0][3].lower()+a[0][4:6].lower(),a[1][0],a[2][0])
#output: N duFort FV

print()

print('----------STR5---------')
str5 = 'DuFort Frankel Von Neumann'
a = str5.upper()
a = a.split()
print(a[-1],a[0][0].lower(),a[1][0].lower(),a[2][0].lower())
#output: NEUMANN d f v

print()

print('----------STR6---------')
str6 = 'duFort Frankel Von Neumann'
a = str6.upper()
a = a.split()
print(a[-1],a[0][0]+a[1][0]+a[2][0])
#output: NEUMANN DFV

print()

print('----------STR7---------')
str7 = '@duFort Frankel Von Neumann$'
a = str7.split()
print(a[0].strip('@'),a[1],a[2],a[-1][0:6].strip('$').upper())
#output: duFort Frankel Von NEUMAN

print()

print('----------STR8---------')
str8 = '#duFort4Frankel4Von4Neumann$'
str8 = str8.strip('#$')
print(str8[0:6],str8[7:14],str8[15:18],str8[19:26])
#output: duFort Frankel Von Neumann


print()

print('----------STR9---------')
str9 = '@duFort@-^Frankel*-(Von(-(Neumann$'
str9 = str9.replace('-', ' ')
str9 = str9.split()
print(str9[0].strip('@'),str9[1].strip('^*'),str9[2].strip('('),str9[3].strip('($'))
#output: duFort Frankel Von Neumann


print()

print
print('----------STR10---------')
str10 = '@DUFort@1^FraNkel*1(VoN(1(NeuMann^'
str10 = str10.replace('1', ' ')
str10 = str10.split()
print(str10[0].strip('@').replace('DU','du'),str10[1].strip('^*').title(),str10[2].strip('(').title(),str10[3].strip('(^').title())
#output: duFort Frankel Von Neumann