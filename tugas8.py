#Data Diri

def Datadiri(nama, alamat, gender, umur, hoby) :
  print("Nama saya :", nama)
  print("temapt tinggal:", alamat)
  print("jenis kelamin:", gender)
  print("umur saya:", umur)
  print("hoby saya:", hoby)

Datadiri("Muhamad Ramadan", "jln.snakma kp.cisalopa", "Laki-Laki", "19", "main futsal")

#Kelulusan Nilai

def mencari_kelulusan(nilai):
 if nilai <= 60:
    print ( "gagal")
 elif 61 <= nilai <= 70 :
    print ("baik")
 elif 71 <= nilai <= 80 :
    print ("sangat baik")
 elif 81 <= nilai <= 100 :
    print ("istimewa")
 else:
    print ("tidak ada")
kkm(60)

#bilangan ganjil

def ganjil(angka) :
   for i in range(angka) :
      if i % 2 != 0 :
         print(i)
ganjil(100)