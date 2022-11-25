namadia = input("Masukkan nama mahasiswa : ")
nimnya = input("Masukkan NIM-nya : ")
string =(nimnya[0:4])

if nimnya[0:2] == '71' and int(nimnya[2:4]) <= 22 and int(nimnya[2:4]) >= 20:
    print(namadia, "Merupakan mahasiswa informatika angkatan 20 hingga 22")
else:
    print(namadia, "bukan mahasiswa informatika angktan 20 hingga 22")