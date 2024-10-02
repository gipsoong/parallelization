from timeit import default_timer as timer
from datetime import timedelta

start = timer()

a = 24
b = 0.25231
c = 100

print(a * b / c)
end = timer()

# print(end-start)
total = (timedelta(seconds=end - start)).total_seconds()
print(f'#1. {total}' + ' second(s)')

def getDuration():
    duration = (timedelta(seconds=end - start)).total_seconds()
    print(f'#2. {duration}' + ' second(s)')


getDuration()