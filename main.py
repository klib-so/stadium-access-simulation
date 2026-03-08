import simpy
import logging
import math
import time

# Constants
QUEUES = 1
QUEUE_CAPACITY = 300
INITIAL_QUEUE_POPULATION = QUEUE_CAPACITY  # Start simulation with full queue to reduce complexity
PLAZA_CAPACITY = 2000
INITIAL_PLAZA_POPULATION = 200
TICKETS_SOLD = 40000  # https://www.footballwebpages.co.uk/premier-league/attendances
STADIUM_CAPACITY = 65000  # https://en.wikipedia.org/wiki/List_of_association_football_stadiums_by_capacity
INITIAL_STADIUM_POPULATION = 2000

# Variables
# Giving time units as proportions of a minute. Will need to standardise this later.
service_time = 3  # Amount of time to check a person's ticket and grant access. To be sampled from a distribution later.
arrival_rate = 20 / 60  # Number of people arriving to plaza every second.           ^^^
start_time = 17 * 60 * 60  # 17:00
end_time = 19 * 60 * 60

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
        self.capacity = STADIUM_CAPACITY
        self.population = INITIAL_STADIUM_POPULATION
        logger.debug(f"The stadium has {self.population} people seated")
        self.plazas = [Plaza(env, self, "North")]  # Directly initialise the list with the Plaza object

    def open_gates(self):
        while (
                (self.plazas[0].population <= PLAZA_CAPACITY)
                and (self.population < TICKETS_SOLD)
                and (self.env.now <= end_time)
        ):
            for plaza in self.plazas:
                for turnstile in plaza.turnstiles:
                    yield self.env.process(turnstile.process_spectator())
                    yield self.env.process(plaza.arrivals())  # Needs to be async I'd say


class Plaza(object):
    def __init__(self, env, stadium, name):
        self.env = env
        self.name = name
        self.stadium = stadium
        self.capacity = PLAZA_CAPACITY
        self.population = INITIAL_PLAZA_POPULATION
        self.turnstile = Turnstile(env, self, "Turnstile A", capacity=1)
        logger.debug(f"{self.name} plaza has {self.population} people")

    def arrivals(self):
        while True:
            yield self.env.timeout(arrival_rate)  # Something like this anyway
            logger.debug(f"Spectator arrived at {format_time(self.env.now)}")
            self.population += 1
            logger.debug(f"{self.name} plaza has {self.population} people")


class Turnstile(simpy.Resource):
    def __init__(self, env, plaza, name, capacity=1):
        super().__init__(env, capacity)
        self.ID = name
        self.env = env
        self.plaza = plaza
        self.queues = [
            Queue(self.env, self.plaza, self, QUEUE_CAPACITY,
                  QUEUE_CAPACITY)]  # Can be turned into a loop if we want more.
        # self.capacity = 1  This is an attribute of simpy.Resource
        self.process_time = service_time

    def process_spectator(self):
        while True:
            logger.debug(f"Began processing spectator at {format_time(self.env.now)}")
            yield self.env.timeout(self.process_time)
            self.admit_spectator()

    def admit_spectator(self):
        logger.debug(f"Spectator admitted at {format_time(self.env.now)}")
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
        logger.debug(f"Queue for {self.turnstile.ID} in {self.plaza.name} plaza moved at {format_time(self.env.now)}")
        self.plaza.population -= 1  # This is kind of hacky, but don't think it needs to be any more complicated for us.
        if True:  # self.plaza.population % 10 == 0:
            # pass
            logger.debug(f"{self.plaza.name} plaza has {self.plaza.population} people")
        # Should collect stat here. Timestamps maybe?
        self.turnstile.process_spectator()


# Helper Functions
def format_time(timestamp):
    timestamp = math.floor(timestamp)
    return time.strftime("%H:%M:%S", time.gmtime(timestamp))
    # hour = (time - (time % 10000))//10000
    # minute = ((time % 10000) - (time % 100))//100
    # second = time % 100
    # return f"{hour}:{minute}:{second}"


# Set up the environment
stadium_env = simpy.RealtimeEnvironment(initial_time=start_time, factor=.008, strict=False)  # Small factors increase the speed. Turning strict off allows very small values.
stadium = Stadium(stadium_env)
stadium_env.process(stadium.open_gates())
stadium_env.run()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    stadium_env.run()
