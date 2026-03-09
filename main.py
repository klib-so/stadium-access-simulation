import simpy
import entities
import configuration as cfg


# Set up the environment
stadium_env = simpy.RealtimeEnvironment(initial_time=cfg.start_time, factor=.008, strict=False)  # Small factors
# increase the speed. Turning strict off allows very small values.
stadium = entities.Stadium(stadium_env)
stadium_env.process(stadium.plazas[0].turnstile.process_spectator())
stadium_env.process(stadium.plazas[0].arrivals())

# Execute
stadium_env.run(until=cfg.end_time)

# For commandline
if __name__ == '__main__':
    stadium_env.run(until=cfg.end_time)
