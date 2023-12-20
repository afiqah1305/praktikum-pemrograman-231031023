biodata = {'Nama'           : 'Afiqah\'',
           'Nim'            : '231031023',
           'Prodi'          : 'Sistem Informasi',
           'TTL'            : 'Sidrap, 13 Mei 2005',
           'Alamat'         : 'Kamirie',
           'Kel/desa'       : 'Mattirotasi',
           'Kecamatan'      : 'Watang Pulu',
           'Hobi'           : 'Membaca',
           'Nama Orang Tua' : {'Ayah' :'Ahmad Mustafa',
                               'Ibu'  : 'Yuliharti',}

        
}

print()
print(biodata)
print()
print(biodata['Nama'])
print(biodata.get('Nim'))
print(biodata.get('prodi'))
print(biodata.get('TTL'))
print(biodata.get('Alamat'))
print(biodata.get('Kel/Desa'))
print(biodata.get('Kecamatan'))
print(biodata['Hobi'])
print(biodata['Nama Orang Tua']['Ayah'])
print(biodata['Nama Orang Tua']['Ibu'])