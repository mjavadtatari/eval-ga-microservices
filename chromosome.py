import random


class Chromosome:
    """ Chromosome Class """

    def __init__(self, microservices_list):
        self.microservices = microservices_list

    def mutation(self, microservice_group):
        index = random.randrange(0, len(self.microservices), 1)
        self.microservices[index] = microservice_group[0].get_random_microservice() # used to be microservice_group.get_random_microservice()

    def fitness(self):
        temp_sum = 0

        for i in self.microservices:
            temp_sum += i.get_response_time()

        return temp_sum

    def crossover(self, another):
        break_point = random.randrange(0, len(self.microservices), 1)

        child_one = Chromosome(self.microservices[:break_point] + another.microservices[break_point:])
        child_two = Chromosome(self.microservices[break_point:] + another.microservices[:break_point])

        return [child_one, child_two]

    def get_gene(self, index):
        return self.microservices[index]

    def get_microservices(self):
        return self.microservices

    def show_chromosome(self):
        temp_list = []

        for i in self.microservices:
            temp_list.append(i.get_response_time())

        return temp_list
