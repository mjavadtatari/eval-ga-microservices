import random
from statistics import mean, mode, median, variance, stdev
from microservice import Microservice


class MicroserviceGroup:
    """ MicroserviceGroup class """
    filter_param = 0

    def __init__(self, microservices_list):
        # self.column_name = column_name
        self.microservices = microservices_list

    def set_microservices(self, microservices_list):
        self.microservices = microservices_list

    def get_microservices(self):
        return self.microservices

    def get_size(self):
        return len(self.microservices)

    def filter_group(self):
        self.set_statistical_indicators()
        tmp_list = []
        for i in self.microservices:
            if i.get_response_time() < self.filter_param:
                tmp_list.append(i)
        return MicroserviceGroup(tmp_list)

    def get_random_microservice(self):
        return self.microservices[random.randrange(0, len(self.microservices), 1)]

    def show_microservice_group(self):
        temp_list = []
        for i in self.microservices:
            temp_list.append(i.get_response_time())
        return temp_list

    def set_statistical_indicators(self):
        """
        msg means microservice group

        median: the middle element of a sorted dataset.
        mode: the value in the dataset that occurs most frequently.
        variance: quantifies the spread of the data. It shows numerically how far the data points are from the mean.
        standard deviation: another measure of data spread. It’s connected to the sample variance, as standard deviation
            , s, is the positive square root of the sample variance.

        """
        decimal_places = 2
        msg_list = [i.get_response_time() for i in self.microservices]
        # mid_index = round(0.5 * self.get_size())

        self.filter_param = msg_list[0]

        msg_statistical_indicators = {
            'min': min(msg_list),
            'max': max(msg_list),
            # 'min': msg_list[0],
            # 'max': msg_list[-1],
            'average': round(mean(msg_list), decimal_places),
            'median': median(msg_list),
            # 'median': [msg_list[mid_index - 1], msg_list[mid_index]] if self.get_size() % 2 else msg_list[mid_index],
            'mode': mode(msg_list),
            'variance': round(variance(msg_list), decimal_places),
            'standard deviation': round(stdev(msg_list), decimal_places),
        }

        # print(self.column_name)
        for key, value in msg_statistical_indicators.items():
            print('{:19}: {}'.format(key, value))
        print('')
