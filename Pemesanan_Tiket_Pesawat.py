# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 20:37:53 2020

@author: HP
"""

import csv

def kota():
    print("Select a City")
    print("Departure \t Arrival")
    print("▶ Jakarta \t ▶ Jakarta")
    print("▶ Makassar \t ▶ Makassar")
    print("▶ Surabaya \t ▶ Surabaya")
    print("▶ Yogyakarta \t ▶ Yogyakarta")
    print("▶ Denpasar \t ▶ Denpasar")
    
def Yogyakarta_Jakarta():
    flights = []
    with open('Yogyakarta_Jakarta.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")
        
def Yogyakarta_Makassar():
    flights = []
    with open('Yogyakarta_Makassar.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")

def Yogyakarta_Surabaya():
    flights = []
    with open('Yogyakarta_Surabaya.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")

def Yogyakarta_Denpasar():
    flights = []
    with open('Yogyakarta_Denpasar.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")
              
def denpasar_jakarta():
    flights = []
    with open('denpasar_jakarta.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")
        
def denpasar_makassar():
    flights = []
    with open('denpasar_makassar.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")
        
def denpasar_surabaya():
    flights = []
    with open('denpasar_surabaya.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")        

def denpasar_yogyakarta():
    flights = []
    with open('denpasar_yogyakarta.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")
              
def makassar_jakarta():
    flights = []
    with open('makassar_jakarta.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")
              
def makassar_surabaya():
    flights = []
    with open('makassar_surabaya.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")
              
def makassar_yogyakarta():
    flights = []
    with open('makassar_yogyakarta.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")
              
def makassar_denpasar():
    flights = []
    with open('makassar_denpasar.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")
              
def jakarta_surabaya():
    flights = []
    with open('jakarta_surabaya.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t {data['PRICE']}")
        
def jakarta_makassar():
    flights = []
    with open('jakarta_makassar.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t {data['PRICE']}")

def jakarta_denpasar():
    flights = []
    with open('jakarta_denpasar.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t {data['PRICE']}")
        
def jakarta_yogyakarta():
    flights = []
    with open('jakarta_yogyakarta.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t {data['PRICE']}")
              
def Surabaya_Jakarta():
    flights = []
    with open('Surabaya_Jakarta.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")
        
def Surabaya_Denpasar():
    flights = []
    with open('Surabaya_Denpasar.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")
        
def Surabaya_Makassar():
    flights = []
    with open('Surabaya_Makassar.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")
        
def Surabaya_Yogyakarta():
    flights = []
    with open('Surabaya_Yogyakarta.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")

def pesan():
    import math
    print("Frequently Added to Booking")
    asuransi_perjalanan = input("◽ Travel Insurance Rp 37.000/pax? (yes/no) : ")
    juml_tiket = penumpang_data
    print("")
    
    if asuransi_perjalanan == "yes":
        asuransi = 37000
    elif asuransi_perjalanan == "no":
        asuransi = 0
    else:
        print ("Please try again")
        
    total_harga = juml_tiket * (harga + asuransi)
    print("Price You Pay Rp", total_harga)
    print("Price Details")
    print("◾ Total Original Price Rp ", math.ceil (juml_tiket * harga))
    print("◾ Insurance Rp ", math .ceil (juml_tiket * asuransi))
       
def data_pemesan():
    print("Contact Details (for E-ticket/Voucher)")
    global pemesan
    pemesan =[]
    nama = input("◾ Full Name : ")
    try:
       nomor = int(input("◾ Mobile Number : +62"))
    except ValueError:
        print("\nError: You have to input your phone number")
    email = input("◾ Email : ")
    pemesan.append(nama)
    pemesan.append(nomor)
    pemesan.append(email)
              
def penumpang():
    print ("Passengers Data")
    penumpang= []
    penumpang_next = True
    while penumpang_next:
        print ("")
        dtpenumpang={}
        name                    = input("Name : ")
        tittle                  = input("Tittle (Mr/Mrs/Ms) : ")
        dtpenumpang['Name'] = name
        dtpenumpang['Tittle'] = tittle
        print ("Passengers Data:", dtpenumpang)
        penumpang.append(dtpenumpang)
        print("Total Passengers:", penumpang)
        
        data = input("Data of Passengers are Complete? (yes/no)")
        if data != "yes":
            penumpang_next = False
            
    cIn = 0
    while cIn < len(penumpang):
        dt = penumpang[cIn]
        cIn += 1
        print()
        print(f"Data penumpang ke-{cIn} :")
        print("NAME :", dt['Name'])
        print("TITTLE :", dt['Tittle'])
              
ulang = True
inputuser = ""

while ulang == True:
    print("\n==================================")
    print(" TRAVELOKE 🛫 BOOK FLIGHT TICKET ")
    print("==================================")
    print("")
    
    kota()
    dari = input("Departure : ")
    ke = input("Arrival : ")
    keberangkatan = str(input("Depatures Date (dd/mm/yyyy): "))
    
    penumpang_data = int(input("Passengers : "))
    print("")
    
    if dari == "Jakarta" and ke == "Surabaya":
        jakarta_surabaya()
        no_pesawat = int(input("Flight Number : "))
        if no_pesawat <= 3:
            harga = 486700
        elif no_pesawat <= 6:
            harga = 1014200
        elif no_pesawat == 7:
            harga = 728000
        elif no_pesawat == 8:
            harga = 1031800
        elif no_pesawat == 9:
            harga = 1071200
        elif no_pesawat == 10:
            harga = 1418700
        else:
            print("Flights are not available")
            
    elif dari == "Jakarta" and ke == "Makassar":
        jakarta_makassar()
        no_pesawat = int(input("Flight Number : "))
        if no_pesawat <= 3:
            harga = 703400
        elif no_pesawat <=7:
            harga = 1600300
        elif no_pesawat == 8:
            harga = 1579400
        elif no_pesawat == 9:
            harga = 1604700
        elif no_pesawat == 10:
            harga = 2148000
        else:
            print("Flights are not available")
    
    elif dari == "Jakarta" and ke == "Denpasar":
        jakarta_denpasar()
        no_pesawat = int(input("Flight Number : "))
        if no_pesawat == 1:
            harga = 1193500
        elif no_pesawat == 2:
            harga = 1218800
        elif no_pesawat == 3:
            harga = 1243900
        elif no_pesawat == 4:
            harga = 1269200
        elif no_pesawat == 5:
            harga = 1293400
        elif no_pesawat <= 10:
            harga = 2148000
        else:
            print("Flights are not available")
            
    elif dari == "Jakarta" and ke == "Yogyakarta":
        jakarta_yogyakarta()
        no_pesawat = int(input("Flight Number : "))
        if no_pesawat <= 3:
            harga = 382200
        elif no_pesawat <=6:
            harga = 705100
        elif no_pesawat == 7:
            harga = 833300
        elif no_pesawat <= 9:
            harga = 802800
        elif no_pesawat == 10:
            harga = 1067800
        else:
            print("Flights are not available")
              
    elif dari == "Makassar" and ke == "Jakarta":
        makassar_jakarta()
        f = open ('makassar_jakarta.csv', 'r')
        reader = csv.reader(f)
        flights = {}
        for row in reader:
            flights[row[0]] = {'airlines':row[1],'time':row[2],'price':row[3]}
        pilih = input("Flight Number : ")
        if pilih in flights:
            print("Airline : ", flights[pilih]['airlines'])
            print("Time    : ", flights[pilih]['time'])
            print("Price   : ", flights[pilih]['price'])
        else:
            print("Flights are not available")
            continue
    
        
    elif dari == "Makassar" and ke == "Surabaya":
        makassar_surabaya()
        f = open ('makassar_surabaya.csv', 'r')
        reader = csv.reader(f)
        flights = {}
        for row in reader:
            flights[row[0]] = {'airlines':row[1],'time':row[2],'price':row[3]}
        pilih = input("Flight Number : ")
        if pilih in flights:
            print("Airline : ", flights[pilih]['airlines'])
            print("Time    : ", flights[pilih]['time'])
            print("Price   : ", flights[pilih]['price'])
        else:
            print("Flights are not available")
            continue
    
    elif dari == "Makassar" and ke == "Yogyakarta":
        makassar_yogyakarta()
       f = open ('makassar_yogyakarta.csv', 'r')
        reader = csv.reader(f)
        flights = {}
        for row in reader:
            flights[row[0]] = {'airlines':row[1],'time':row[2],'price':row[3]}
        pilih = input("Flight Number : ")
        if pilih in flights:
            print("Airline : ", flights[pilih]['airlines'])
            print("Time    : ", flights[pilih]['time'])
            print("Price   : ", flights[pilih]['price'])
        else:
            print("Flights are not available")
            continue
            
    elif dari == "Makassar" and ke == "Denpasar":
        makassar_denpasar()
        f = open ('makassar_denpasar.csv', 'r')
        reader = csv.reader(f)
        flights = {}
        for row in reader:
            flights[row[0]] = {'airlines':row[1],'time':row[2],'price':row[3]}
        pilih = input("Flight Number : ")
        if pilih in flights:
            print("Airline : ", flights[pilih]['airlines'])
            print("Time    : ", flights[pilih]['time'])
            print("Price   : ", flights[pilih]['price'])
        else:
            print("Flights are not available")
            continue
              
    elif dari == "Surabaya" and ke == "Jakarta":
        Surabaya_Jakarta()
        no_pesawat = int(input("Flight Number : "))
        if no_pesawat <= 5:
            harga = 476700
        elif no_pesawat <= 9:
            harga = 1054200
        elif no_pesawat == 10:
            harga = 1378700
        else:
            print("Flights are not available")
            
    elif dari == "Surabaya" and ke == "Makassar":
        Surabaya_Makassar()
        no_pesawat = int(input("Flight Number : "))
        if no_pesawat <= 5:
            harga = 522900
        elif no_pesawat == 6:
            harga = 1144400
        elif no_pesawat == 7:
            harga = 1008000
        elif no_pesawat == 8:
            harga = 1174100
        elif no_pesawat == 9:
            harga = 1245600
        elif no_pesawat == 10:
            harga = 1732500
        else:
            print("Flights are not available")
    
    elif dari == "Surabaya" and ke == "Denpasar":
        Surabaya_Denpasar()
        no_pesawat = int(input("Flight Number : "))
        if no_pesawat <= 5:
            harga = 457400
        elif no_pesawat == 6:
            harga = 582300
        elif no_pesawat == 7:
            harga = 607600
        elif no_pesawat <= 9:
            harga = 832400
        elif no_pesawat == 10:
            harga = 1258600
        else:
            print("Flights are not available")
            
    elif dari == "Surabaya" and ke == "Yogyakarta":
        Surabaya_Yogyakarta()
        no_pesawat = int(input("Flight Number : "))
        if no_pesawat <= 6:
            harga = 623000
        elif no_pesawat <= 8:
            harga = 724200
        elif no_pesawat == 9:
            harga = 1056300
        elif no_pesawat == 10:
            harga = 1618700
        else:
            print("Flights are not available")
              
    elif dari == "Yogyakarta" and ke == "Jakarta":
        Yogyakarta_Jakarta()
        f = open('Yogyakarta_Jakarta.csv', 'r')
        reader = csv.reader(f)
        flights = {}
        for row in reader:
            flights[row[0]] = {'airlines':row[1],'time':row[2],'price':row[3]}
        pilih = input("Flight Number : ")
        if pilih in flights:
            print("Airline : ", flights[pilih]['airlines'])
            print("Time    : ", flights[pilih]['time'])
            print("Price   : ", flights[pilih]['price'])
        else:
            print("Flights are not available")
            continue
        
    elif dari == "Yogyakarta" and ke == "Makassar":
        Yogyakarta_Makassar()
        f = open('Yogyakarta_Makassar.csv', 'r')
        reader = csv.reader(f)
        flights = {}
        for row in reader:
            flights[row[0]] = {'airlines':row[1],'time':row[2],'price':row[3]}
        pilih = input("Flight Number : ")
        if pilih in flights:
            print("Airline : ", flights[pilih]['airlines'])
            print("Time    : ", flights[pilih]['time'])
            print("Price   : ", flights[pilih]['price'])
        else:
            print("Flights are not available")
            continue
    
    elif dari == "Yogyakarta" and ke == "Surabaya":
        Yogyakarta_Surabaya()
        f = open('Yogyakarta_Surabaya.csv', 'r')
        reader = csv.reader(f)
        flights = {}
        for row in reader:
            flights[row[0]] = {'airlines':row[1],'time':row[2],'price':row[3]}
        pilih = input("Flight Number : ")
        if pilih in flights:
            print("Airline : ", flights[pilih]['airlines'])
            print("Time    : ", flights[pilih]['time'])
            print("Price   : ", flights[pilih]['price'])
        else:
            print("Flights are not available")
            continue
            
    elif dari == "Yogyakarta" and ke == "Denpasar":
        Yogyakarta_Denpasar()
        f = open('Yogyakarta_Denpasar.csv', 'r')
        reader = csv.reader(f)
        flights = {}
        for row in reader:
            flights[row[0]] = {'airlines':row[1],'time':row[2],'price':row[3]}
        pilih = input("Flight Number : ")
        if pilih in flights:
            print("Airline : ", flights[pilih]['airlines'])
            print("Time    : ", flights[pilih]['time'])
            print("Price   : ", flights[pilih]['price'])
        else:
            print("Flights are not available")
            continue
    
    elif dari == "Denpasar" and ke == "Jakarta":
        denpasar_jakarta()
        f = open('denpasar_jakarta.csv', 'r')
        reader = csv.reader(f)
        flights = {}
        for row in reader:
            flights[row[0]] = {'airlines':row[1],'time':row[2],'price':row[3]}
        pilih = input("Flight Number : ")
        if pilih in flights:
            print("Airline : ", flights[pilih]['airlines'])
            print("Time    : ", flights[pilih]['time'])
            print("Price   : ", flights[pilih]['price'])
        else:
            print("Flights are not available")
            continue
        
    elif dari == "Denpasar" and ke == "Makassar":
        denpasar_makassar()
        f = open('denpasar_makassar.csv', 'r')
        reader = csv.reader(f)
        flights = {}
        for row in reader:
            flights[row[0]] = {'airlines':row[1],'time':row[2],'price':row[3]}
        pilih = input("Flight Number : ")
        if pilih in flights:
            print("Airline : ", flights[pilih]['airlines'])
            print("Time    : ", flights[pilih]['time'])
            print("Price   : ", flights[pilih]['price'])
        else:
            print("Flights are not available")
            continue
    
    elif dari == "Denpasar" and ke == "Surabaya":
        denpasar_surabaya()
        f = open('denpasar_surabaya.csv', 'r')
        reader = csv.reader(f)
        flights = {}
        for row in reader:
            flights[row[0]] = {'airlines':row[1],'time':row[2],'price':row[3]}
        pilih = input("Flight Number : ")
        if pilih in flights:
            print("Airline : ", flights[pilih]['airlines'])
            print("Time    : ", flights[pilih]['time'])
            print("Price   : ", flights[pilih]['price'])
        else:
            print("Flights are not available")
            continue
    
    elif dari == "Denpasar" and ke == "Yogyakarta":
        denpasar_yogyakarta()
        f = open('denpasar_yogyakarta.csv', 'r')
        reader = csv.reader(f)
        flights = {}
        for row in reader:
            flights[row[0]] = {'airlines':row[1],'time':row[2],'price':row[3]}
        pilih = input("Flight Number : ")
        if pilih in flights:
            print("Airline : ", flights[pilih]['airlines'])
            print("Time    : ", flights[pilih]['time'])
            print("Price   : ", flights[pilih]['price'])
        else:
            print("Flights are not available")
            continue
              
    print("")
    pesan()
    print("")
    data_pemesan()
    print("")
    penumpang()
    
    inputuser = input("Back to Menu? (yes/no) : ")
    if inputuser != "yes":
        ulang = False
        
print("")
print ("Thank You")
              

              
