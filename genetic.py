from chromosome import Chromosome


class Genetic:
    ''' Genetic Class '''

    populations = []

    def __init__(self, microservicegroup_list):
        self.microservicegroups = microservicegroup_list

        for i in range(0, 30):
            temp_list = []
            for j in self.microservicegroups:
                temp_list.append(j.get_random_microservice())
            temp_chromosome = Chromosome(temp_list)
            self.populations.append(temp_chromosome)

    def set_genetic(self):
        pass

    def get_genetic(self):
        pass

    def show_population(self):
        temp_list = []
        for i in self.populations:
            temp_list.append(i)
            # temp_i=[]
            # for j in i.get_microservices():
            #     temp_i.append(j.get_response_time())
            # temp_list.append(temp_i)

        return temp_list
