import random
from microservice import Microservice


class MicroserviceGroup:
    """ MicroservicGroup class """

    def __init__(self, microservices_list):
        self.microservices = microservices_list

    def set_microservices(self, microservices_list):
        self.microservices = microservices_list

    def get_microservices(self):
        return self.microservices

    def get_size(self):
        return len(self.microservices)

    def filter_group(self, response_time):
        tmp_list = []
        for i in self.microservices:
            if i.get_response_time() < response_time:
                tmp_list.append(i)
        return MicroserviceGroup(tmp_list)

    def get_random_microservice(self):
        return self.microservices[random.randrange(0, len(self.microservices), 1)]

    def show_microservice_group(self):
        temp_list = []
        for i in self.microservices:
            temp_list.append(i.get_response_time())
        return temp_list
