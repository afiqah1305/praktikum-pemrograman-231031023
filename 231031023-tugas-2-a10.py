# Fungsi untuk mengubah waktu dalam format "HH:MM" atau "HH.MM" menjadi menit
def konversi_waktu(time_str):
    if ':' in time_str:
        hours, minutes = map(int, time_str.split(':'))
    else:
        hours, minutes = map(int, time_str.split('.'))
    return hours * 60 + minutes

# Fungsi untuk mengubah menit menjadi waktu dalam format "HH:MM"
def format_waktu(minutes):
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02d}:{minutes:02d}"

# Fungsi untuk menambahkan waktu ke waktu awal
def tambah_waktu(waktu_awal, waktu_tambahan):
    waktu_awal_minutes = konversi_waktu(waktu_awal)
    waktu_tambahan_minutes = konversi_waktu(waktu_tambahan)
    waktu_hasil_minutes = (waktu_awal_minutes + waktu_tambahan_minutes) % 1440
    waktu_hasil = format_waktu(waktu_hasil_minutes)
    return waktu_hasil

# Fungsi untuk menghitung selisih waktu dari waktu awal
def selisih_waktu_fn(waktu_awal, selisih_waktu):
    waktu_awal_minutes = konversi_waktu(waktu_awal)
    selisih_waktu_minutes = konversi_waktu(selisih_waktu)
    waktu_hasil_minutes = (waktu_awal_minutes - selisih_waktu_minutes) % 1440
    waktu_hasil = format_waktu(waktu_hasil_minutes)
    return waktu_hasil

# Input waktu awal
waktu_awal = input("Masukkan waktu awal (HH:MM atau HH.MM): ")

# Input pilihan
print("Pilih operasi:")
print("1. Penjumlahan waktu")
print("2. Selisih waktu")
pilihan = input("Masukkan pilihan (1/2): ")

if pilihan == '1':
    waktu_tambahan = input("Masukkan waktu tambahan (HH:MM): ")
    waktu_hasil = tambah_waktu(waktu_awal, waktu_tambahan)
    print("Waktu sekarang menunjukkan Pukul " + waktu_hasil)
elif pilihan == '2':
    selisih_waktu = input("Masukkan selisih waktu (HH:MM): ")
    waktu_hasil = selisih_waktu_fn(waktu_awal, selisih_waktu)
    print("Waktu sekarang menunjukkan Pukul " + waktu_hasil)
else:
    print("Pilihan tidak valid.")
