## contoh soal
# 1. ----- 0 ++++++ 5 ----- 8 ++++++ 11 ----
soalpertama = float(input("masukan angka untuk soal pertama : "))

lebih0 = soalpertama > 0
kurang5 = soalpertama < 5
lebih8 = soalpertama > 8
kurang11 = soalpertama < 11

angkasoal = lebih0 and kurang5 or lebih8 and kurang11
print("angka anda termasuk kedalam nilai : ", angkasoal)



# 2. +++++ 0 ----- 5 +++++ 8 ----- 11 +++++
soalkedua = float(input("masukan angka untuk soal kedua : "))
kurang0 = soalkedua < 0
lebih5 = soalkedua > 5
kurang8 = soalkedua < 8
lebih11 = soalkedua > 11

hasilsoal = kurang0 or lebih5 and kurang8 or lebih11
print("angka anda termasuk kedalam nilai : ", hasilsoal)