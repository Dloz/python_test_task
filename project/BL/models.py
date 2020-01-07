from datetime import datetime
from decimal import Decimal

class Call:
    '''
    Represents model of a call.
    '''
    def __init__(self, caller_number, target_number, call_started_time, call_ended_time, connection_type):
        self.caller_number = caller_number
        self.target_number = target_number
        self.call_started_time = self.__convert_date_to_str(call_started_time)
        self.call_ended_time = self.__convert_date_to_str(call_ended_time)
        self.connection_type = connection_type
        self.cost = None


    def set_cost(self, cost):
        '''
        Set cost of a call.
        '''
        self.cost = cost
    

    def get_call_duration(self):
        '''
        Method to receive duration of the call model.
        Returns:
            Duration of the call model.
        '''
        end_time = datetime.strptime(self.call_ended_time, "%Y-%m-%d %H:%M:%S").timestamp()
        start_time = datetime.strptime(self.call_started_time, "%Y-%m-%d %H:%M:%S").timestamp()

        return Decimal(end_time - start_time)

    
    def __convert_date_to_str(self, timestamp):
        '''
        Private method which converts from timestamp object to string in format %Y-%m-%d %H:%M:%S
        '''
        date_str = datetime.fromtimestamp(timestamp)
        return date_str.strftime('%Y-%m-%d %H:%M:%S')
    
    
    def __str__(self):
        return "{}, {}, {}, {}, {}".format(
            self.caller_number,
            self.target_number,
            self.call_started_time,
            self.call_ended_time,
            self.connection_type,
            )