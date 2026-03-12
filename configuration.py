# Log level
# log_level = "DEBUG"  # Looks like an enum


# Constants
PLAZAS = ["Block A", "Block B", "Block C", "Block D"]
QUEUE_CAPACITY = 300
INITIAL_QUEUE_POPULATION = QUEUE_CAPACITY  # Start simulation with full queue to reduce complexity
PLAZA_CAPACITY = 3000
INITIAL_PLAZA_POPULATION = 800
TURNSTILES = 6
TICKETS_SOLD = 40000  # https://www.footballwebpages.co.uk/premier-league/attendances
STADIUM_CAPACITY = 65000  # https://en.wikipedia.org/wiki/List_of_association_football_stadiums_by_capacity
INITIAL_STADIUM_POPULATION = 4000

# Variables
# Giving time units as proportions of a minute. Will need to standardise this later.
service_time = 10  # Amount of time to check a person's ticket and grant access. To be sampled from a distribution later.
arrival_rate = 20 / 60  # Number of people arriving to plaza every second.           ^^^
start_time = 17 * 60 * 60  # 17:00
end_time = 19 * 60 * 60
