from memory_profiler import profile

@profile
def memory_demo():
    large = bytearray(20_000_000)
    backup = large
    del large
    del backup

memory_demo()
