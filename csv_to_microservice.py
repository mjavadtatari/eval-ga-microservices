import csv
from microservice import Microservice

# global variables
CSV_FILE_ADDRESS = 'sample-data.csv'

rows_without_headers = []
microservices_list = []

with open(CSV_FILE_ADDRESS, 'r') as f:
    for i in csv.reader(f):
        rows_without_headers.append(i)

    rows_without_headers.pop(0)


for i in rows_without_headers:
    microservices_list.append(Microservice(i[1:]))

for i in microservices_list:
    print(i.to_str())