import random
from genetic import Genetic
from microservice import Microservice
from microservice_group import MicroserviceGroup
from csv_to_microservice import get_data

a = get_data()

# a = [Microservice(random.randrange(1, 1000, 1)) for i in range(0, 4)]
# b = [Microservice(random.randrange(1, 1000, 1)) for i in range(0, 4)]
# c = [Microservice(random.randrange(1, 1000, 1)) for i in range(0, 4)]
# d = [Microservice(random.randrange(1, 1000, 1)) for i in range(0, 4)]

# p =[]
# p.append(MicroserviceGroup(a))
# p.append(MicroserviceGroup(b))
# p.append(MicroserviceGroup(c))
# p.append(MicroserviceGroup(d))

genetic = Genetic(a)

print(genetic.run().show_chromosome())
#
# print(genetic.show_population()[0].show_chromosome())
#
# genetic.population_sort()
#
# print(genetic.show_population()[0].show_chromosome())
#
# genetic.show_population()[0].mutation(a[0])
#
# print(genetic.show_population()[0].show_chromosome())
