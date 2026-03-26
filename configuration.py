# Log level
# log_level = "DEBUG"  # Looks like an enum


# Constants
# Adjust these!
# Adding plaza names to the list processes them automatically.
PLAZAS = ["Block A"]#, "Block B"]
QUEUE_CAPACITY = 300  # This does nothing right now, but can easily be made to.
INITIAL_QUEUE_POPULATION = 0  # Set these to zero to debug the distributions. Will require small bit of code to get
# working. Nothing major.
PLAZA_CAPACITY = 3000  # Again, this has no effect at the moment, but would just take a few minutes to add the logic.
INITIAL_PLAZA_POPULATION = 0  # Set these to zero to debug the distributions.
TURNSTILES = 8  # Global number of turnstiles per plaza. Can be split out into variable per plaza if we want.
TICKETS_SOLD = 5000  # https://www.footballwebpages.co.uk/premier-league/attendances
STADIUM_CAPACITY = 8000  # https://en.wikipedia.org/wiki/List_of_association_football_stadiums_by_capacity
INITIAL_STADIUM_POPULATION = 0  # Set these to zero to debug the distributions.
HOURS = 60 ** 2
MINUTES = 60


# Variables
# Adjust these!
arrival_standard_deviation = 9.1971*MINUTES
min_service_time = 3  # Minimum amount of time (in seconds) to check a person's ticket and grant access.
service_rate = 0.61

start_time = 17 * HOURS + 0 * MINUTES  # 17:00. Replace zero with minutes.
end_time = 19 * HOURS + 0 * MINUTES
kickoff_time = 19 * HOURS + 0 * MINUTES
earliest_arrival = 120  # In minutes before kickoff. NOT USED
mean_arrival_time_before_kickoff = 37*MINUTES #11.807 * MINUTES  # In minutes.
late_arrival_offset = 5  # In minutes after kickoff. NOT USED


# These are computed for use in the code.
first_arrival_absolute_time = kickoff_time - earliest_arrival * MINUTES
last_arrival = kickoff_time + late_arrival_offset * MINUTES
mean_absolute_arrival_time = kickoff_time - mean_arrival_time_before_kickoff
service_scale = 1/service_rate


# Output options
arrival_output = True
processing_output = True
queue_length_output = True
stadium_population_output = False
all_output = False
