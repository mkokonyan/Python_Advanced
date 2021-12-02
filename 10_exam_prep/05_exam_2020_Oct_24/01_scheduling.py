import sys

jobs = [int(x) for x in input().split(", ")]
job_index = int(input())

clock_cycles = 0
while True:
    min_job = min(jobs)
    current_min_index = jobs.index(min_job)
    clock_cycles += jobs[current_min_index]
    if not current_min_index == job_index:
        jobs[current_min_index] = sys.maxsize
    else:
        break
print(clock_cycles)
