import math
import time


# Helper Functions
def format_time(timestamp):
    timestamp = math.floor(timestamp)
    return time.strftime("%H:%M:%S", time.gmtime(timestamp))
    # hour = (time - (time % 10000))//10000
    # minute = ((time % 10000) - (time % 100))//100
    # second = time % 100
    # return f"{hour}:{minute}:{second}"
