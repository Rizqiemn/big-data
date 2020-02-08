def cetak_nilai(nama, twitter,*scores):
    print("Nama : "+nama+"\nTwitter : "+twitter+"\nScore yang diperoleh : ")
    i=1
    for score in scores:
        print("nilai ke -%d : %d "%(i,score))
        i=i+1
    return;

#kalau poarameter diisi semua
print("Tentang variabel length, variabel sisa akan menjadi tuple")
cetak_nilai('Rizqie','@Rizqiemn',1400,100,250,356)