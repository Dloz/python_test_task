

class Call:
    
    def __init__(self, caller_number, target_number, start_call_time, end_call_time, connection_type):
        self.caller_number = caller_number
        self.target_number = target_number
        self.start_call_time = start_call_time
        self.end_call_time = end_call_time
        self.connection_type = connection_type