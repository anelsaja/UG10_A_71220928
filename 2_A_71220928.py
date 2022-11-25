print('===== Selamat datang di Toko Andi tersenyum, selamat belanja ! =====')
z=int(input('Total belanja :Rp.'))


q = z - (z*2/100)
w = z - (z*5/100)
e = z - (z*10/100)

if z < 100000:
    print("Tidak ada diskon! Maka yang anda bayarkan adalah: Rp. ", z)
elif z >= 500000:
    print('Biaya yang harus dibayarkan setelah diskon adalah: Rp. ',w)
elif z <= 100000:
    print('Biaya yang harus dibayarkan setelah diskon adalah: Rp. ',q)
elif z > 999999:
    print("Tidak ada diskon! Maka yang anda bayarkan adalah: Rp. ", e)