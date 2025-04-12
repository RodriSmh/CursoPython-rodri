import csv
with open("datos.csv", encoding="utf-8") as archivo:
    for row in csv.reader(archivo):
        print(row)