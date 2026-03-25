import math
import time
import numpy as np
from scipy.stats import norm
import configuration as cfg
import stadium_entities


# Helper Functions
def format_time(timestamp):
    timestamp = math.floor(timestamp)
    return time.strftime("%H:%M:%S", time.gmtime(timestamp))


def format_percent(numerator, denominator):
    adj = '%s' % float('%.2g' % (100 * numerator / denominator))
    return f"{adj}%"


# Distributions
def get_service_time(min_wait):
    return np.random.exponential(scale=cfg.service_scale, size=None) + min_wait
    # return 5


def get_arrival_interval(population, env_time):
    centre_point = cfg.mean_absolute_arrival_time
    sd = cfg.arrival_standard_deviation
    return norm.ppf((population + 1) / cfg.TICKETS_SOLD, loc=centre_point, scale=sd) - env_time

