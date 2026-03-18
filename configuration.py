# Log level
# log_level = "DEBUG"  # Looks like an enum


# Constants
PLAZAS = ["Block A"] #, "Block B", "Block C", "Block D", "Block E", "Block F"]
QUEUE_CAPACITY = 300
INITIAL_QUEUE_POPULATION = 0  # Start simulation with full queue to reduce complexity
PLAZA_CAPACITY = 3000
INITIAL_PLAZA_POPULATION = 0
TURNSTILES = 1
TICKETS_SOLD = 40000  # https://www.footballwebpages.co.uk/premier-league/attendances
STADIUM_CAPACITY = 65000  # https://en.wikipedia.org/wiki/List_of_association_football_stadiums_by_capacity
INITIAL_STADIUM_POPULATION = 0

# Variables
# Giving time units as proportions of a minute. Will need to standardise this later.
min_service_time = 3  # Minimum amount of time to check a person's ticket and grant access.
arrival_rate = 20 / 60  # Number of people arriving to plaza every second.
start_time = 17 * 60 * 60  # 17:00
end_time = 19 * 60 * 60
mean_absolute_arrival_time = end_time - 60*60  # The average time a spectator arrives in seconds. As in 18:15.


