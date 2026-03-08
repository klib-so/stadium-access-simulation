import simpy
import logging
import functions as fn
import configuration as cfg

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# Environment
class Stadium(object):
    def __init__(self, env):
        self.env = env
        self.capacity = cfg.STADIUM_CAPACITY
        self.population = cfg.INITIAL_STADIUM_POPULATION
        logger.debug(f"The stadium has {self.population} people seated")
        self.plazas = [Plaza(env, self, "North")]  # Directly initialise the list with the Plaza object

    # def open_gates(self):
    #     while (
    #             (self.plazas[0].population <= PLAZA_CAPACITY)
    #             and (self.population < TICKETS_SOLD)
    #     ):
    #         for plaza in self.plazas:
    #             for turnstile in plaza.turnstiles:
    #                 for en in turnstile.process_spectator():
    #                     yield en
    #                 # yield next(plaza.arrivals())  # Needs to be async I'd say


class Plaza(object):
    def __init__(self, env, stadium, name):
        self.env = env
        self.name = name
        self.stadium = stadium
        self.capacity = cfg.PLAZA_CAPACITY
        self.population = cfg.INITIAL_PLAZA_POPULATION
        self.turnstile = Turnstile(env, self, "Turnstile A", capacity=1)
        logger.debug(f"{self.name} plaza has {self.population} people")

    def arrivals(self):
        while True:
            yield self.env.timeout(1/cfg.arrival_rate)  # Something like this anyway
            logger.debug(f"Spectator arrived at {fn.format_time(self.env.now)}")
            self.population += 1
            logger.debug(f"{self.name} plaza has {self.population} people")


class Turnstile(simpy.Resource):
    def __init__(self, env, plaza, name, capacity=1):
        super().__init__(env, capacity)
        self.ID = name
        self.env = env
        self.plaza = plaza
        self.queues = [
            Queue(self.env, self.plaza, self, cfg.QUEUE_CAPACITY,
                  cfg.QUEUE_CAPACITY)]  # Can be turned into a loop if we want more.
        # self.capacity = 1  This is an attribute of simpy.Resource
        self.process_time = cfg.service_time

    def process_spectator(self):
        while True:
            logger.debug(f"Began processing spectator at {fn.format_time(self.env.now)}")
            yield self.env.timeout(self.process_time)
            self.admit_spectator()

    def admit_spectator(self):
        logger.debug(f"Spectator admitted at {fn.format_time(self.env.now)}")
        self.plaza.stadium.population += 1  # This is a bit weird the way it is called. Can refactor later.
        # Stadium has turnstiles, that have queues, that have plazas?

        if True:  # self.plaza.stadium.population % 10 == 0:
            logger.debug(f"The stadium has {self.plaza.stadium.population} people seated")
        # self.release(request)
        self.queues[0].move_queue()  # Emit event here


class Queue(object):
    def __init__(self, env, plaza, turnstile, capacity, initial_pop):
        self.env = env
        self.plaza = plaza
        self.turnstile = turnstile
        self.capacity = capacity
        self.population = initial_pop

    def move_queue(self):
        logger.debug(f"Queue for {self.turnstile.ID} in {self.plaza.name} plaza moved at {fn.format_time(self.env.now)}")
        self.plaza.population -= 1  # This is kind of hacky, but don't think it needs to any more complicated for us.
        if True:  # self.plaza.population % 10 == 0:
            # pass
            logger.debug(f"{self.plaza.name} plaza has {self.plaza.population} people")
        # Should collect stat here. Timestamps maybe?
        # with self.turnstile.request() as req:
        #     yield req
        #     # yield self.env.process(self.turnstile.process_spectator())
