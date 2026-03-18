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
    # hour = (time - (time % 10000))//10000
    # minute = ((time % 10000) - (time % 100))//100
    # second = time % 100
    # return f"{hour}:{minute}:{second}"


def format_percent(num):
    adj = '%s' % float('%.2g' % (num * 100))
    return f"{adj}%"


# Distributions
def get_service_time(min_wait):
    return np.random.exponential(scale=5.0, size=None) + min_wait
    # return 5


def get_arrival_interval(current_time):
    centre_point = cfg.mean_absolute_arrival_time
    sd = (cfg.end_time - cfg.start_time) / 6
    return float(len(cfg.PLAZAS) / (cfg.TICKETS_SOLD * norm.pdf(current_time, loc=centre_point, scale=sd)))


def process_spectator(plaza, spec_id):
    if plaza.population > 0:
        stadium_entities.logger.debug(
            f"{plaza.name} turnstile began processing spectator {spec_id} at {format_time(plaza.env.now)}")
        yield plaza.env.timeout(get_service_time(cfg.min_service_time))  # Yield to simulate service time
        admit_spectator(plaza, spec_id)  # Admit the spectator after processing


def admit_spectator(plaza, spec_id):
    stadium_entities.logger.debug(f"Spectator {spec_id} admitted to {plaza.name} at {format_time(plaza.env.now)}")
    plaza.population -= 1  # Update population count
    plaza.stadium.population += 1  # Update stadium population if necessary
    stadium_entities.logger.debug(
        f"Current stadium population: {format_percent(plaza.stadium.population / cfg.TICKETS_SOLD)}")
