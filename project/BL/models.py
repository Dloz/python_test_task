print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))


class Call:
    
    def __init__(self, caller_number, target_number, start_call_time, end_call_time, connection_type):
        self.caller_number = caller_number
        self.target_number = target_number
        self.start_call_time = start_call_time
        self.end_call_time = end_call_time
        self.connection_type = connection_type
        self.cost = None


    def set_cost(self, cost):
        self.cost = cost
    

    def get_call_duration(self):
        return self.end_call_time - self.start_call_time
    
    
    def __str__(self):
        return "{}, {}, {}, {}, {}".format(
            self.caller_number,
            self.target_number,
            self.start_call_time,
            self.end_call_time,
            self.connection_type,
            )