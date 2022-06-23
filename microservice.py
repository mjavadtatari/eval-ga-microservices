class Microservice:
    """ Microservices class """

    def __init__(self, time):
        """
        attribute = k
        """
        self.response_time = time
        # self.reliability = None
        # self.price = None

    def to_str(self):
        return str(self.__dict__)

    def set_response_time(self, time):
        self.response_time = time

    def get_response_time(self):
        return self.response_time

    # def get_reliability(self):
    #     return self.reliability
    #
    # def get_price(self):
    #     return self.price

    def get_value(self):
        return self.response_time / 100
