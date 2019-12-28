import os, sys

#Following lines are for assigning parent directory dynamically.

dir_path = os.path.dirname(os.path.realpath(__file__))

parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))

sys.path.insert(0, parent_dir_path)

from DAL.models import Tariff



def calculate(call_duration, connection_type):
    '''Every call costs something. This method calculates cost of the call 
    depending on connection type and duration of the call.


    Args:
        call_duration: Duration of the call in seconds.
        connection_type: Type of call connection.


    Returns:
        cost: cost of call depending on income arguments.
    '''
    cost = get_cost(connection_type)
    
    #Divide by 60 to convert from seconds to minutes
    return cost * call_duration // 60 

def get_cost(connection_type):
    tariff = Tariff.query.filter_by(connection_type=connection_type).first()
    return tariff.price


if __name__ == '__main__':
    cost = calculate(280, "LTE")
    print(cost)