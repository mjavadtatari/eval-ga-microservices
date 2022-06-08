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
        for i in self.microservices:
            if i.get_response_time() > response_time:
                self.microservices.pop(i)

    def get_random_microservice(self):
        return self.microservices[random.randrange(0, len(self.microservices), 1)]
