"""
Tipe data dictionary sekedar link antara KEY dan VALUE
KVP = key value pari
dictionary = kamus
"""

kamus_ind_eng = {'anak': 'son', 'istri': 'wife', 'ayah': 'father', 'paman': 'uncle', 'ibu': 'mother'}

print(kamus_ind_eng)
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['ibu'])
# 'merk': [{'kar9k'},{'magnum'}] ga bisa harus 2
print('\nData barang di toko warfire, di antaranya :')
data_toko_barang = {
    'tanggal': '2020-06-07',
    'jenis_barang': [
        {'senjata': 'shotgun', 'merk': 'AWM'},
        {'senjata': 'sniper', 'merk': 'kar9k'},
        {'senjata': 'pistol', 'merk': 'dual'},
        {'senjata': 'machine_gun', 'merk': 'minigun'}
    ]
}
print(data_toko_barang)
print(f"Jenis barang di toko {data_toko_barang['jenis_barang']}")
print(f"\nJenis #1 {data_toko_barang['jenis_barang'][0]}")
print(f"merk sniper ini {data_toko_barang['jenis_barang'][1]['merk']}")
print(f"Jenis #3 {data_toko_barang['jenis_barang'][3]}")
