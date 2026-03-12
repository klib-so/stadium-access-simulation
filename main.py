import simpy
import entities
import configuration as cfg


# Set up the environment
stadium_env = simpy.RealtimeEnvironment(initial_time=cfg.start_time, factor=.008, strict=False)  # Small factors
# increase the speed. Turning strict off allows very small values.
stadium = entities.Stadium(stadium_env)
for plaza in stadium.plazas:
    for queue in plaza.turnstile.queues:
        stadium_env.process(queue.run())
    stadium_env.process(plaza.arrivals())

# Execute
stadium_env.run(until=cfg.end_time)

# For commandline
if __name__ == '__main__':
    stadium_env.run(until=cfg.end_time)
