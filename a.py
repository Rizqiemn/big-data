"""Seleksi"""
"""umur = int(input("Masukkan Umur Anda = "))
if (umur <=5):kriteria='Balita'
if (umur >5 and umur <=13):kriteria='Anak-anak'
if (umur >13 and umur <=25):kriteria='Remaja'
if (umur >25 and umur <=35):kriteria='Dewasa'
if (umur >35 and umur <=55):kriteria='Orang tua'
if (umur >55 and umur <=300):kriteria='Lansia'
if (umur >300):kriteria='Abadi'

print('Umur= %d tahun dan kriteria yaitu %s' %(umur,kriteria))
"""

#Perulangan sebanyak 5 kali
for i in [1,2,3,4,5]:
    print('Ini perulangan ke-',i)

print('\n________________________________\n')
#Perulangan sebanyak 5 kali
for i in ['Informatika - S1','Sistem Informasi - S1','Sistem Informasi - D3','Teknik Komputer - S1','Teknik Elektro - S1','Data Science - S1']:
    print(i, ' adalah prodi pada FTIE-UTY')

print('\n________________________________\n')
    #Perulangan sebanyak 5 kali
for i in range(1,5):
    print('(RANGE Ini perulangan ke-',i)

print('\n________________________________\n')
    #Perulangan sebanyak 5 kali
for i in 'ABCDE':
    print(i,' ADALAH ALFABET')

print('\n________________________________\n')
itr=1
epoch=8
while(itr<epoch):
    print('ini iterasi ke- ',itr)
    itr+=1