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
        self.counter = 0
        logger.debug(f"The stadium has {fn.format_percent(self.population / cfg.TICKETS_SOLD)} of people seated")
        self.plazas = []
        for plaza_name in cfg.PLAZAS:
            self.plazas.append(Plaza(env, self, plaza_name))

    def simulate(self):
        for plaza in self.plazas:
            self.env.process(plaza.arrivals())



class Plaza(object):
    def __init__(self, env, stadium, name):
        # super().__init__(env)
        self.env = env
        self.name = name
        self.stadium = stadium
        self.capacity = cfg.PLAZA_CAPACITY
        self.population = cfg.INITIAL_PLAZA_POPULATION
        self.turnstile = Turnstile(env, self, f"{self.name} Turnstile", capacity=cfg.TURNSTILES)
        # self.turnstile = simpy.Resource(self.env, capacity=cfg.TURNSTILES)
        logger.debug(f"{self.name} plaza starts with {self.population} people waiting")


    def arrivals(self):
        while True:
            yield self.env.timeout(fn.get_arrival_interval(self.env.now))  # Arrival interval
            self.stadium.counter += 1
            spec_id = self.stadium.counter
            logger.debug(f"Spectator {spec_id} arrived at {self.name} plaza at time {fn.format_time(self.env.now)}")
            self.population += 1  # Update population count
            logger.debug(f"{self.name} plaza has {self.population} people")
            self.env.process(self.que_arrival(spec_id))


    def que_arrival(self, spec_id):
        # if len(self.turnstile.queue)/self.turnstile.capacity <= cfg.QUEUE_CAPACITY:
        #     yield self.env.timeout((cfg.QUEUE_CAPACITY - len(self.turnstile.queue))/(10 * self.turnstile.capacity))  # Time to walk to join the queue.
            # This will break if we breach queue capacity!!!
        with self.turnstile.request() as req:
            logger.debug(f"Spectator {spec_id} joins que")
            yield req
            yield self.env.process(self.turnstile.process_spectator(spec_id))


class Turnstile(simpy.Resource):
    def __init__(self, env, plaza, name, capacity=1):
        super().__init__(env, capacity)
        self.ID = name
        self.env = env
        self.plaza = plaza
        self.min_process_time = cfg.min_service_time
        # self.turnstile_free = self.env.event()
        # self.process_spectator()

    def process_spectator(self, spec_id):
        if self.plaza.population > 0:
            logger.debug(f"{self.plaza.name} turnstile began processing spectator {spec_id} at {fn.format_time(self.env.now)}")
            yield self.plaza.env.timeout(fn.get_service_time(self.min_process_time))
            self.admit_spectator(spec_id)


    def admit_spectator(self, spec_id):
        logger.debug(f"Spectator {spec_id} admitted to {self.plaza.name} at {fn.format_time(self.env.now)}")
        self.plaza.population -= 1
        self.plaza.stadium.population += 1  # This is a bit weird the way it is called. Can refactor later.
        # Stadium has turnstiles, that have queues, that have plazas?

        if True:  # self.plaza.stadium.population % 10 == 0:
            logger.info(
                f"The stadium has {fn.format_percent(self.plaza.stadium.population / cfg.TICKETS_SOLD)} people seated")
