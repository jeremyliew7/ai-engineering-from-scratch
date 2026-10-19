import tracemalloc

tracemalloc.start()
small = bytearray(100_000)
large = bytearray(1_000_000)

snapshot = tracemalloc.take_snapshot()
for stat in snapshot.statistics("lineno")[:3]:
    print(stat)
tracemalloc.stop()
