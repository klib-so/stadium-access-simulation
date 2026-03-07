import simpy
import logging

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
service_time = 3 / 60  # Amount of time to check a person's ticket and grant access. To be sampled from a distribution later.
arrival_rate = 20 / 60  # Number of people arriving to plaza every minute.           ^^^

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# Environment
class Stadium(object):
    def __init__(self, env):
        self.env = env
        self.capacity = STADIUM_CAPACITY
        self.population = INITIAL_STADIUM_POPULATION
        logger.info(f"The stadium has {self.population} people seated")
        self.plazas = [Plaza(env, self, "North")]  # Directly initialise the list with the Plaza object

    def open_gates(self):
        while (self.plazas[0].population <= PLAZA_CAPACITY) and (self.population < TICKETS_SOLD):
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
        self.turnstiles = [Turnstile(env, self, "Turnstile A")]
        logger.info(f"Plaza:  {self.name} has {self.population} people")

    def arrivals(self):
        # logger.info(f"Spectator arrived at {self.env.now}")
        self.population += 1
        # logger.info(f"Plaza {self.name} has {self.population} people")
        yield self.env.timeout(arrival_rate)  # Something like this anyway


class Turnstile:
    def __init__(self, env, plaza, name):
        self.ID = name
        self.env = env
        self.plaza = plaza
        self.queues = [
            Queue(self.env, self.plaza, self, QUEUE_CAPACITY,
                  QUEUE_CAPACITY)]  # Can be turned into a loop if we want more.
        self.capacity = 1
        self.process_time = service_time

    def process_spectator(self):
        # logger.info(f"Began processing spectator at {self.env.now}")
        yield self.env.timeout(self.process_time)
        self.admit_spectator()

    def admit_spectator(self):
        # logger.info(f"Spectator admitted at {self.env.now}")
        self.plaza.stadium.population += 1  # This is a bit weird the way it is called. Can refactor later. Stadium has turnstiles, that have queues, that have plazas?
        if self.plaza.stadium.population % 1000 == 0:
            logger.info(f"The stadium has {self.plaza.stadium.population} people seated")
        self.queues[0].turnstile_free()


class Queue(object):
    def __init__(self, env, plaza, turnstile, capacity, initial_pop):
        self.env = env
        self.plaza = plaza
        self.turnstile = turnstile
        self.capacity = capacity
        self.population = initial_pop

    def turnstile_free(self):
        # logger.info(f"Queue moved at {self.env.now}")
        self.plaza.population -= 1  # This is kind of hacky, but don't think it needs to any more complicated for us.
        if self.plaza.population % 10 == 0:
            pass
            # logger.info(f"Plaza: {self.plaza.name} has {self.plaza.population} people")
        # Should collect stat here. Timestamps maybe?
        self.turnstile.process_spectator()

        # Probably queues should be a resource
        # Leave this till the classes look right. We can probably extend the simpy classes.
        # self.turnstile = simpy.Resource(env, QUEUES)


# Set up the environment
stadium_env = simpy.Environment()
stadium = Stadium(stadium_env)
stadium_env.process(stadium.open_gates())
stadium_env.run()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    stadium_env.run()

