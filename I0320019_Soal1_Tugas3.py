# Menampilkan list 10 teman
list = ['Candrika','Aratia','Angela','Gea','Divana','Hana','Funny','Ayu','Adrian','Afiq']

# Menampilkan isi list indeks nomor 4,6,7
print("List indeks nomor 4,6, dan 7 yaitu", list[4],",", list[6], ",", "dan", list[7])

# Mengganti nama teman di list 3,5, dan 9
list[3] = 'Audrey'
list[5] = 'Bonang'
list[6] = 'Attar'

# Menambahkan 2 nama teman
list.append('Bagus')
list.append('Evelyn')

# Menampilkan semua teman dengan pengulangan
print(list*2)

# Menampilkan panjang list
print(len(list))