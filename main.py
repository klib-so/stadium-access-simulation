import simpy
import stadium_entities
import configuration as cfg
import functions as fn


# Set up the environment
stadium_env = simpy.Environment(initial_time=cfg.start_time)  # Small factors
# increase the speed. Turning strict off allows very small values. 0.008 seems good.
stadium = stadium_entities.Stadium(stadium_env)

# Process Simulation
stadium.simulate()

# Execute
try:
    stadium_env.run(until=cfg.end_time)
except ValueError:
    print(f"Simulation exited at {fn.format_time(stadium_env.now)} with {fn.format_percent(stadium.population)} people "
          f"seated, and {stadium.plazas[0].population} waiting for access."
          )
# For commandline
if __name__ == '__main__':
    try:
        stadium_env.run(until=cfg.end_time)
    except ValueError:
        print(f"Simulation exited at {fn.format_time(stadium_env.now)} with {fn.format_percent(stadium.population)}"
              f" people seated, and {stadium.plazas[0].population} waiting for access."
              )
