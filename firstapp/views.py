from django.shortcuts import render

# Create your views here.

import csv
#from . models import Date_Store

def Test(request):
    with open('C:/Users/HP/Desktop/CSV/out1 django.csv') as csv_file:
        cv = csv.reader(csv_file, delimiter=',')
        all_value = []
        for row in cv:
            data = row[1::]
            print(data)

print("hello")