# Membuat dictionary pada python
dict = {'Nama':'Candrika','Hobi1':'Menulis','Hobi2':'Membaca','Hobi3':'Menonton film','Hobi4':'Jalan-jalan',
        'Sosmed1':'ig:@candrikaa18','Sosmed2':'line:candrikaaa','Sosmed3':'twitter:hallolalun','Lagu1':'To My Youth',
        'Lagu2':'Saturday Night','Lagu3':'Bertaut','Makanan1':'Seblak','Makanan2':'Nasi Goreng','Makanan3':'Sushi'}

#Mengubah salah satu hobi dan sosmed, menghapus 2 makanan, dan menambah 1 hobi
dict['Hobi3'] = 'Tidur'
dict['Sosmed1'] = 'ig:@hallolaluna'
del dict['Makanan2']
del dict['Makanan3']
dict['Hobi4'] = 'Mengaji'

print(dict)