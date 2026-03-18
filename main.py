import simpy
import stadium_entities
import configuration as cfg


# Set up the environment
stadium_env = simpy.Environment(initial_time=cfg.start_time)  # Small factors
# increase the speed. Turning strict off allows very small values. 0.008 seems good.
stadium = stadium_entities.Stadium(stadium_env)

# Process Simulation
stadium.simulate()

# Execute
stadium_env.run(until=cfg.end_time)

# For commandline
if __name__ == '__main__':
    stadium_env.run(until=cfg.end_time)
