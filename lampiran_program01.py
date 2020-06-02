# -*- coding: utf-8 -*-
"""
Created on Thu May  7 23:00:00 2020

@author: User
"""

datanilai = []
datanilai_next = True
i = 0
while datanilai_next :
    print ("")
    dtnilai = {}
    nim                     = input("Input NIM : ")
    nama                    = input("Input Nama : ")
    tugas                   = int(input("Input Nilai Tugas : "))
    uts                     = int(input("Input Nilai UTS : "))
    uas                     = int(input("Input Nilai UAS : "))
    dtnilai['NIM']          = nim
    dtnilai['Nama']         = nama
    dtnilai['Nilai Tugas']  = tugas
    dtnilai['Nilai UTS']    = uts
    dtnilai['Nilai UAS']    = uas
    print("Data Mahasiswa : ", dtnilai)
    datanilai.append(dtnilai)
    print('Data Nilai Mahasiswa : ', datanilai)
    
    nextdata = input("Tambah data lagi? (y/t)")
    if nextdata != 'y':
        datanilai_next = False
        
print(datanilai)

cIn = 0
while cIn < len(datanilai):
    dt = datanilai[cIn]
    cIn += 1
    print()
    print(f"Data Mahasiswa ke-{cIn} :")
    print("NIM :", dt['NIM'])
    print("Nama :", dt['Nama'])
    print("Nilai Tugas :", dt['Nilai Tugas'])
    print("Nilai UTS :", dt['Nilai UTS'])
    print("Nilai UAS :", dt['Nilai UAS'])
    
    na = tugas*0.25 + uts*0.35 + uas*0.40

    if na >= 80:
        print("Nilai Akhir",na,"Huruf A")
    elif na >= 70:
        print("Nilai Akhir",na,"Huruf B")
    elif na >= 60:
        print("Nilai Akhir",na,"Huruf C")
    elif na >= 50:
        print("Nilai Akhir",na,"Huruf D")
    else:
        print("Nilai Akhir",na,"Huruf E")
    
    
    