from timeit import default_timer as timer
from datetime import timedelta

start = timer()

a = 24
b = 0.25231
c = 100

print(a * b / c)
end = timer()


def getDuration():
    duration = (timedelta(seconds=end - start)).total_seconds()
    print(f'Executed in: {duration}' + ' second(s)')


getDuration()
