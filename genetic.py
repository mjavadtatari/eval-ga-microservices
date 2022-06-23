import random

from chromosome import Chromosome


class Genetic:
    """ Genetic Class """

    populations = []

    def __init__(self, microservicegroup_list):
        temp_list = []
        for i in microservicegroup_list:
            temp_list.append(i.filter_group())

        self.microservicegroups = temp_list

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
            temp_list.append(i.show_chromosome())
            print(i.show_chromosome())
            # temp_i=[]
            # for j in i.get_microservices():
            #     temp_i.append(j.get_response_time())
            # temp_list.append(temp_i)
            # print(i.show_chromosome())
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
                first_parent = self.populations[random.randint(0, len(self.populations) - 1)]
                second_parent = self.populations[random.randint(0, len(self.populations) - 1)]
                new_childes = first_parent.crossover(second_parent)
                self.populations.append(new_childes[0])
                self.populations.append(new_childes[1])

            y = self.selection()
            for i in range(int(y)):
                # mutation(self.microservicegroups)
                self.mutation(self.populations[random.randint(0, len(self.populations) - 1)])

            self.fitness()
            # print('\n\nGen #{}:'.format(g + 1))
            # self.show_population()
            # print(self.show_population())

            # for idx, i in enumerate(self.microservicegroups):
            #     print("MSG #{}: ".format(idx + 1))
            #     i.set_statistical_indicators()
            #     print('')
        for i in self.microservicegroups:
            i.find_quality_degree_matrix(4)
            i.find_probability_matrix('negative', 'response_time')
            i.normalize_quality_degree('response_time')

        return self.populations[0]

    def mutation(self, chromosome):
        index = random.randrange(0, chromosome.chromosome_size(), 1)
        temp_chromosome = Chromosome(chromosome.microservices)
        temp_chromosome.mutation(self.microservicegroups[index], index)
        self.populations.append(temp_chromosome)
        # print(type(temp_chromosome))
