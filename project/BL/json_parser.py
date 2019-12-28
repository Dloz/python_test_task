import json
from BL.models import Call


def parse(json_data):
    loaded_json = (json.loads(json_data))
    call = Call(
        loaded_json["caller_number"],
        loaded_json["target_number"],
        loaded_json["call_start_time"],
        loaded_json["call_ended_time"],
        loaded_json["connection_type"],
    )    
    return call


if __name__ == '__main__':
    json_data = """{ "caller_number": "123456",
    "target_number": "1234",
    "call_start_time": 1577366700,
    "call_ended_time": 1577366900,
    "connection_type": "LTE"
    }"""

    parse(json_data)