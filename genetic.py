import random

from chromosome import Chromosome


class Genetic:
    """ Genetic Class """

    populations = []

    def __init__(self, microservicegroup_list):
        self.microservicegroups = microservicegroup_list

        for i in range(0, 30):
            temp_list = []
            for j in self.microservicegroups:
                temp_list.append(j.get_random_microservice())
            temp_chromosome = Chromosome(temp_list)
            self.populations.append(temp_chromosome)

    def fitness(self):
        self.population_sort()

    def population_sort(self):
        temp_list = {}
        new_population = []

        for idx, i in enumerate(self.populations):
            temp_list[i.fitness()] = idx

        for key in sorted(temp_list.keys()):
            new_population.append(self.populations[temp_list[key]])

        self.populations = new_population

        # for i in self.populations:
        #     print(i.fitness())

    def terminate(self, stop_point):
        if self.populations[0].fitness() < stop_point:
            return True
        return False

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

    def selection(self):
        return len(self.populations) * 0.1

    def run(self):
        stop_point = 40
        generation = 10

        for g in range(generation):
            self.fitness()
            if self.terminate(stop_point):
                return self.populations[0]

            x = self.selection()
            for i in range(int(x)):
                first_parent = self.populations[random.randint(0, len(self.populations)-1)]
                second_parent = self.populations[random.randint(0, len(self.populations)-1)]
                new_childes = first_parent.crossover(second_parent)
                self.populations.append(new_childes[0])
                self.populations.append(new_childes[1])

            y = self.selection()
            for i in range(int(y)):
                self.populations[random.randint(0, len(self.populations)-1)].mutation(self.microservicegroups)

        return self.populations[0]
