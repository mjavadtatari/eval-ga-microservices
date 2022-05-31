class Microservice:
    ''' Microservices class '''

    def __init__(self, data_array):
        # class attributes
        self.gateway = None
        self.ticket_reserve = None
        self.ticket_explore = None
        self.security = None
        self.ticket_info = None
        self.order = None
        self.basic_info = None
        self.config = None
        self.station = None
        self.train = None
        self.contact = None
        self.price = None

        i = 0

        for key in self.__dict__.keys():
            setattr(self, key, data_array[i])
            i += 1

    def to_str(self):
        return str(self.__dict__)