#terdiri dari 4 kondisi
#NOT, And, OR, XOR

#untuk kondisi ++++++3--------10++++++++++

inputUser = float(input ("masukan angka yang \n kurang dari 3\n atau \n lebih dari 10 \n :"))

# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("angka kurang dari 3 = ", isKurangDari)

# memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("angka lebih dari 10 = ", isLebihDari)

#kondisi dengan or untuk gabungan keduanya
isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukan :", isCorrect)




#untuk kondisi ---------3++++++++++10----------
inputUser2 = float(input("Masukan angka diantara 3 dan 10 : "))

#Kondisi pertama ----3++++++++++
KondisiPertama = inputUser2 > 3
print ("Angka lebih dari 3 :", KondisiPertama)

#kondisi kedua ++++++++++10------- 
KondisiKedua = inputUser2 < 10
print ("angka kurang dari 10 :", KondisiKedua)

#Kondisi gabungan keduanya
KondisiGabungan = KondisiPertama and KondisiKedua
print ("angka diantara 3 dan 10 :", KondisiGabungan)