import random

# from statistics import mean, mode, median, variance, stdev
from microservice import Microservice


class MicroserviceGroup:
    """
    MicroserviceGroup class
    also called Task class
    """
    quality_of_service = {}
    quality_degree_matrix = {}
    probability_matrix = {}
    normalized_matrix = {}
    filter_param = 600

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
        # self.filter_param[str(ms_attribute) + '_min'] = min_param
        # self.filter_param[str(ms_attribute) + '_max'] = max_param
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

        # self.filter_param = msg_list[0]

        msg_statistical_indicators = {
            'min': min(msg_list),
            'max': max(msg_list),
            # 'min': msg_list[0],
            # 'max': msg_list[-1],
            # 'average': round(mean(msg_list), decimal_places),
            # 'median': median(msg_list),
            # 'median': [msg_list[mid_index - 1], msg_list[mid_index]] if self.get_size() % 2 else msg_list[mid_index],
            # 'mode': mode(msg_list),
            # 'variance': round(variance(msg_list), decimal_places),
            # 'standard deviation': round(stdev(msg_list), decimal_places),
        }

        # print(self.column_name)
        for key, value in msg_statistical_indicators.items():
            print('{:19}: {}'.format(key, value))
        print('')

    def set_quality_of_service(self, ms_attribute, weight, constraint):
        self.quality_of_service[str(ms_attribute)] = [weight, constraint]

    def find_quality_degree_matrix(self, degree_steps):
        """
        response_time is negative_quality_property
        reliability is positive_quality_property
        price is negative_quality_property
        """

        response_msg_list = [i.get_response_time() for i in self.microservices]
        temp_steps = (max(response_msg_list) - min(response_msg_list)) // degree_steps
        self.quality_degree_matrix['response_time'] = list(
            range(min(response_msg_list), max(response_msg_list), temp_steps))
        print('response_time: min: {}, max:{}, steps:{} | '.format(min(response_msg_list), max(response_msg_list),
                                                                   temp_steps), end="")
        print(self.quality_degree_matrix['response_time'])
        del response_msg_list

        # reliability_msg_list = [i.get_reliability() for i in self.microservices]
        # temp_steps = (max(reliability_msg_list) - min(reliability_msg_list)) // degree_steps
        # self.quality_degree_matrix['reliability'] = range(min(reliability_msg_list), max(reliability_msg_list),
        #                                                   temp_steps)
        # del reliability_msg_list
        #
        # price_msg_list = [i.get_price() for i in self.microservices]
        # temp_steps = (max(price_msg_list) - min(price_msg_list)) // degree_steps
        # self.quality_degree_matrix['price'] = range(min(price_msg_list), max(price_msg_list), temp_steps)
        # del price_msg_list

    def find_probability_matrix(self, prop_type, prop_name):
        """

        :param prop_type: like 'positive' or 'negative'
        :param prop_name: like 'response_time'
        """
        temp_probability_list = []
        get_prop = getattr(Microservice, 'get_' + prop_name)
        # print(get_prop(self.microservices[0]))

        for degree in self.quality_degree_matrix[prop_name]:
            temp_degree = 0
            for i in self.microservices:
                if get_prop(i) >= degree and prop_type == 'positive':
                    temp_degree += 1
                elif get_prop(i) <= degree and prop_type == 'negative':
                    temp_degree += 1
            temp_probability_list.append(round(temp_degree / self.get_size(), 2))

        self.probability_matrix[prop_name] = temp_probability_list
        print('response_time_probability: {}'.format(self.probability_matrix))

    def normalize_quality_degree(self, prop_name):
        temp_list = []
        for i in range(len(self.probability_matrix[prop_name])):
            temp_list.append(round(self.probability_matrix[prop_name][i] * self.quality_degree_matrix[prop_name][i], 2))
        self.normalized_matrix = temp_list
        print('{}\n'.format(self.normalized_matrix))
