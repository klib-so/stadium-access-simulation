import math
import time
import numpy as np
from scipy.stats import norm
import configuration as cfg


# Helper Functions
def format_time(timestamp):
    timestamp = math.floor(timestamp)
    return time.strftime("%H:%M:%S", time.gmtime(timestamp))
    # hour = (time - (time % 10000))//10000
    # minute = ((time % 10000) - (time % 100))//100
    # second = time % 100
    # return f"{hour}:{minute}:{second}"


def format_percent(num):
    adj = '%s' % float('%.2g' % (num * 100))
    return f"{adj}%"


# Distributions
def get_service_time(min):
    return np.random.exponential(scale=5.0, size=None) + min


def get_arrival_interval(current_time):
    centre_point = cfg.mean_absolute_arrival_time
    sd = (cfg.end_time - cfg.start_time) / 6
    # arrivals_remaining = cfg.TICKETS_SOLD - cfg.INITIAL_STADIUM_POPULATION - cfg.TURNSTILES*len(cfg.PLAZAS)*cfg.QUEUE_CAPACITY
    return float(1 / ((cfg.TICKETS_SOLD/len(cfg.PLAZAS)) * norm.pdf(current_time, loc=centre_point, scale=sd)))
