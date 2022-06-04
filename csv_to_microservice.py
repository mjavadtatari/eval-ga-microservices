import csv
from microservice import Microservice
from microservice_group import MicroserviceGroup

# global variables
CSV_FILE_ADDRESS = 'sample-data.csv'

rows_without_headers = []
microservicesgroup_list = []

with open(CSV_FILE_ADDRESS, 'r') as f:
    for i in csv.reader(f):
        rows_without_headers.append(i)

    rows_without_headers.pop(0)

for col in range(1,13):
    microservices_list = []
    for i in rows_without_headers:
        microservices_list.append(Microservice(i[col]))
    microservicesgroup_list.append(MicroserviceGroup(microservices_list))
    


# for i in range(len(microservicesgroup_list)):
#     print('{0}: {1}'.format(i, microservicesgroup_list[i]))


def get_data():
    global microservicesgroup_list
    return microservicesgroup_list