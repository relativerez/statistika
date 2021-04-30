def menu():
    print("1.input data")
    print("2.tampilkan data")
    print("3.operasi statistika data")
    print("4.exit program")

data = []

def insert_data():
  n = int(input("masukan jumlah angka untuk diurutkan: "))
  for i in range(n):
    nilai = int(input("masukkan angka ke-" + str(i+1) + ': '))
  data.append(nilai)

def median(angka):
    return float(sum(angka)) / max(len(angka), 1)

def rata_rata (angka):
  return sum(angka) / len(angka)

def nilai_maksimal(deret_bilangan):
  nilai_terbesar = deret_bilangan[0]

  for nilai in deret_bilangan:
    if nilai > nilai_terbesar:
      nilai_terbesar = nilai

  return nilai_terbesar

def nilai_minimal(deret_bilangan):
  nilai_terkecil = deret_bilangan[0]

  for nilai in deret_bilangan:
    if nilai < nilai_terkecil:
      nilai_terkecil = nilai

  return nilai_terkecil

def modus(deret):
  # dictionary untuk mapping nilai terbanyak
  peta_kemunculan = {}

  # perulangan satu-persatu tiap bilangan
  for bilangan in deret:
    # periksa apakah sudah pernah muncul atau belum
    if bilangan in peta_kemunculan:
      peta_kemunculan[bilangan] += 1
    else:
      peta_kemunculan[bilangan] = 1

  # cari kemunculan terbanyak
  bilangan_terbesar = deret[0] # ambil angka pertama sebagai yg terbanyak
  for bilangan in peta_kemunculan.keys():
    jumlah = peta_kemunculan[bilangan]

    if jumlah > peta_kemunculan[bilangan_terbesar]:
      bilangan_terbesar = bilangan

  return bilangan_terbesar

def frekuensi(data):
    return {i: data.count(i) for i in data}

def tampilan():
  print("nilai rata-rata: ",rata_rata(data))
  print("nilai maksimal: ",nilai_maksimal(data))
  print("nilai minimal: ",nilai_minimal(data))
  print("median: ",median(data))
  print("modus: ",modus(data))
  print("frekuensi: ",frekuensi(data))
  print("-----lanjutkan inputan data----")

loop = 1
pilihan = 0
while loop == 1:
  menu()
  pilihan = int(input('masukan pilihan: '))
  if pilihan == 1 :
    insert_data()
  elif pilihan == 2 :
    print(data)
  elif pilihan == 3 :
    tampilan()
  elif pilihan == 4 :
    yakin = input('Ingin keluar? (y/n) ')
    if yakin == 'y':
      loop = 0
  else:
    print('maaf pilihan anda tidak ada dimenu')



# print("nilai rata-rata: ",rata_rata(data))
# print("nilai maksimal: ",nilai_maksimal(data))
# print("nilai minimal: ",nilai_minimal(data))
# print("median: ",median(data))
# print("modus: ",modus(data))
# print("frekuensi: ",frekuensi(data))



# import statistics

# data = [1,2,3,4]

# x = statistics.mean(data)
# print(x)

# data = []
# jum = 0
# n = int(input(" angka : "))
# def nil_rata():
#     for i in range(0, n):
#     temp = int(input("masukkan angka ke-" + str(i+1) + ': '))
#     data.append(temp)
#     jum += data[i]
#     rata2 = jum / n


# mean = []

# n = int(input(" angka : "))


# # harus ada median,nilai rata_rata,nilai maksimal dan minimal, modus sama frekuensi
# for i in range(n):
#     nilai = int(input("masukkan angka ke-" + str(i+1) + ': '))
#     mean.append(nilai)

# print(median(mean))
# print(rata2)