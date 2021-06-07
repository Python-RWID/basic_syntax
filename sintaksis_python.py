print('\nconstruction basic python')
print('Hello world')
print("by Fauzan")
print('-' * 3)

print('\npercabangan eksekusi terpilih')
success = True
if success :
    print('maka belajarlah dengan giat')
else:
    print ('maka bermalas - malasan lah')

print('\nPERCABANGAN PILIHAN LEBIH DARI 2 / LOOP')
Jumlah_anak = 4

for index_anak in range(1,Jumlah_anak+1): #jumplah loop = 5 - 1 = 4
    print(f'halo anak {index_anak}')

print('\ntipe-data list / skalar => tipe data sederhana')
anak1 = 'akhmad'
anak2 = 'fauzan'
anak3 = 'farhan'

print (anak1)
print (anak2)
print (anak3)

print('\ntipe data list/array/daftar')
anak = ['nabila', 'nadia', 'amalia']
print(anak)
anak.append('paijo')
print(anak)

print('\nmemanggil salah satu object')
print(f'Hai {anak[1]}, apa kabar ?')

print('\nmemanggil banyak object')
for z in anak :
    print(f'Hai {z}!')

print('\nmemanggil banyak object cara ke-2')
for z in range (0, len(anak)):
    print(f'{z+1}.Hai {anak[z]}')