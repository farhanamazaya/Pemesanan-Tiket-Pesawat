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
