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
    
def Yogyakarta_Jakarta():
    import csv
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
    import csv
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
    import csv
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
    import csv
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
    import csv
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
    import csv
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
    import csv
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
    import csv
    flights = []
    with open('denpasar_yogyakarta.csv') as csv_file:
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
        no_pesawat = int(input("Flight Number : "))
        if no_pesawat == 1:
            harga = 1293100
        elif no_pesawat <= 3:
            harga = 332200
        elif no_pesawat <= 5:
            harga = 451000
        elif no_pesawat == 6:
            harga = 655600
        elif no_pesawat == 7:
            harga = 754600
        elif no_pesawat == 8:
            harga = 767800
        elif no_pesawat <= 10:
            harga = 987800
        else:
            print("Flights are not available")
        
    elif dari == "Yogyakarta" and ke == "Makassar":
        Yogyakarta_Makassar()
        no_pesawat = int(input("Flight Number : "))
        if no_pesawat <= 2:
            harga = 500500
        elif no_pesawat <= 4:
            harga = 935600
        elif no_pesawat == 5:
            harga = 1045000
        elif no_pesawat <= 7:
            harga = 1248940
        elif no_pesawat == 8:
            harga = 1645900
        elif no_pesawat <= 10:
            harga =  2269900
        else:
            print("Flights are not available")
    
    elif dari == "Yogyakarta" and ke == "Surabaya":
        Yogyakarta_Surabaya()
        no_pesawat = int(input("Flight Number : "))
        if no_pesawat <= 3:
            harga = 718900
        elif no_pesawat <= 6:
            harga = 1723200
        elif no_pesawat == 7:
            harga = 2276500
        elif no_pesawat <= 9:
            harga = 583000
        elif no_pesawat == 10:
            harga = 1217200
        else:
            print("Flights are not available")
            
    elif dari == "Yogyakarta" and ke == "Denpasar":
        Yogyakarta_Denpasar()
        no_pesawat = int(input("Flight Number : "))
        if no_pesawat <= 2:
            harga = 992200
        elif no_pesawat == 3:
            harga = 1279300
        elif no_pesawat == 4:
            harga = 1262781
        elif no_pesawat == 5:
            harga = 1307216
        elif no_pesawat == 6:
            harga = 1317344
        elif no_pesawat <= 8:
            harga = 522448
        elif no_pesawat <= 10:
            harga = 2063300
        else:
            print("Flights are not available")
    
    elif dari == "Denpasar" and ke == "Jakarta":
        denpasar_jakarta()
        no_pesawat = int(input("Flight Number : "))
        if no_pesawat == 1:
            harga = 486700
        elif no_pesawat == 2:
            harga = 1258900
        elif no_pesawat == 3:
            harga = 1268800
        elif no_pesawat == 4:
            harga = 1284200
        elif no_pesawat <= 6:
            harga = 1293000
        elif no_pesawat == 7:
            harga = 1308400
        elif no_pesawat <= 10:
            harga = 1679100
        else:
            print("Flights are not available")
        
    elif dari == "Denpasar" and ke == "Makassar":
        denpasar_makassar()
        no_pesawat = int(input("Flight Number : "))
        if no_pesawat == 1:
            harga = 754000
        elif no_pesawat == 2:
            harga = 982800
        elif no_pesawat == 3:
            harga = 1092800
        elif no_pesawat <= 6:
            harga = 1396400
        elif no_pesawat == 7:
            harga = 1654400
        elif no_pesawat == 8:
            harga = 2167000
        elif no_pesawat <= 10:
            harga = 3697100
        else:
            print("Flights are not available")
    
    elif dari == "Denpasar" and ke == "Surabaya":
        denpasar_surabaya()
        no_pesawat = int(input("Flight Number : "))
        if no_pesawat == 1:
            harga = 592300
        elif no_pesawat == 2:
            harga = 611000
        elif no_pesawat == 3:
            harga = 617600
        elif no_pesawat == 4:
            harga = 641800
        elif no_pesawat <= 10:
            harga = 2967800
        else:
            print("Flights are not available")
    
    elif dari == "Denpasar" and ke == "Yogyakarta":
        denpasar_yogyakarta()
        no_pesawat = int(input("Flight Number : "))
        if no_pesawat == 1:
            harga = 834400
        elif no_pesawat <= 5:
            harga = 1042200
        elif no_pesawat == 6:
            harga = 1093900
        elif no_pesawat == 7:
            harga = 1329300
        elif no_pesawat <= 10:
            harga = 2616900
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
              

              
