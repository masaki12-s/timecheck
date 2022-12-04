class Timecheck:
    def __init__(self):
        return self

    def check(time, start_time, end_time)->str:
        if start_time <= end_time and start_time <= time < end_time:
            return "OK"
        elif end_time <= start_time and (( start_time <= time and end_time < time ) or ( time <= start_time and time < end_time)):
            return "OK"
        else:
            return "NG"
    
    def dupcheck(time, start_time, end_time)->str:
        if start_time <= end_time and start_time <= time < end_time:
            return "OK"
        elif end_time <= start_time and (( start_time <= time and end_time < time ) or ( time <= start_time and time < end_time)):
            return "OK"
        else:
            return "NG"


