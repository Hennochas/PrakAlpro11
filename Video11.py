#Hennoch Azarya Saragih
#71200636
#Universitas Kristen Duta Wacana
#Sumber : Buat sendiri 

'''
Mervin adalah mahasiswa akutansi di suatu universitas lalu dia diberi sebuah data oleh dosennya
dia pun disuruh mencari berapa jumlah angka pada data tersebut, saya sebagai mahasiswa informatika
akan membantu mervin menyelesaikan problemnya.

'''
'''
Input : Angka berapa yang akan dicari

Proses : Mengunakan perulangan for lalu mengukan if untuk mencari angka tersebut

Output : Jumlah angka yang dicari
'''
def mencari_jumlah(tup, x):
    count = 0 
    for elemen in tup:
        if (elemen == x):
            count = count + 1
    return count

tup = (10, 8, 5, 7, 9, 5, 6, 8, 0, 2, 7, 3)
dicari = 6
dicari1 = 0
dicari2 = 3
print(mencari_jumlah(tup,dicari))
print(mencari_jumlah(tup,dicari1))
print(mencari_jumlah(tup,dicari2))