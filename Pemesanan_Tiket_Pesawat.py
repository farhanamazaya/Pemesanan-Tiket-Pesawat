# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 20:37:53 2020

@author: HP
"""

def kota():
    print("Select a City")
    print("Departure \t Arrival")
    print("▶ Jakarta \t ▶ Jakarta")
    print("▶ Makassar \t ▶ Makassar")
    print("▶ Surabaya \t ▶ Surabaya")
    print("▶ Yogyakarta \t ▶ Yogyakarta")
    print("▶ Denpasar \t ▶ Denpasar")
    
def yia_cgk():
    import csv
    flights = []
    with open('yiacgk.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")
        
def yia_upg():
    import csv
    flights = []
    with open('yiaupg.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")

def yia_sub():
    import csv
    flights = []
    with open('yiasub.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")

def yia_dps():
    import csv
    flights = []
    with open('yiadps.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")
def dps_cgk():
    import csv
    flights = []
    with open('dpscgk.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")
        
def dps_upg():
    import csv
    flights = []
    with open('dpsupg.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")
        
def dps_sub():
    import csv
    flights = []
    with open('dpssub.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")        

def dps_yia():
    import csv
    flights = []
    with open('dpsyia.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")
              
def upg_cgk():
    import csv
    flights = []
    with open('upgcgk.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")
              
def upg_sub():
    import csv
    flights = []
    with open('upgsub.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")
              
def upg_yia():
    import csv
    flights = []
    with open('upgyia.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")
              
def upg_dps():
    import csv
    flights = []
    with open('upgdps.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")
              
def jakarta_surabaya():
    import csv
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
    import csv
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
    import csv
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
    import csv
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
    import csv
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
    import csv
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
    import csv
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
    import csv
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
    input("◾ Full Name : ")
    input("◾ Mobile Number : ")
    input("◾ Email : ")
    print("""We will send your booking confirmations to the above contact details, 
which will also be used for refund or reschedule purposes.""")
              
def penumpang():
    penumpang= []
    penumpang_next = True
    while penumpang_next:
        print ("")
        dtpenumpang={}
        name                    = input("Name : ")
        tittle                  = input("Tittle : ")
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
              

              
