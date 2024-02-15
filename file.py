import csv 
from datetime import datetime

file_path = 'c:/Users/shyam/OneDrive/Desktop/PYTHON/samples.csv'  
fi = open(file_path, 'r')
       
lines = fi.readlines()

for line in lines:
    current_date_time = datetime.now()
    coloumn = line.split()
    print(coloumn[2],current_date_time)
