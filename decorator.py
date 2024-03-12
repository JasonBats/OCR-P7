import time
import tracemalloc


def perfs_decorator(func):
    def wrapper():
        tracemalloc.start()  # Start memory tracking
        ping = time.perf_counter()  # Start time tracking
        func()
        _, peak = tracemalloc.get_traced_memory()  # Store memory peak.
        pong = time.perf_counter()  # Stop time tracking
        tracemalloc.stop()  # Stop memory tracking
        print(f'Peak : {peak / 1048576:.2f} MB')
        print(f'Temps écoulé : {pong - ping:0.2f} secondes')

    return wrapper
