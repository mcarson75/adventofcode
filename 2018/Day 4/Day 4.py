import re

with open("input.txt", "r", encoding="utf-8") as f:
    lines = [l.strip() for l in f.readlines()]

lines.sort()

guard_pattern = r"\[\d{4}\-\d{2}\-\d{2} \d{2}:\d{2}\] Guard #(\d+) begins shift"
sleep_pattern = r"\[\d{4}\-\d{2}\-\d{2} \d{2}:(\d{2})\] falls asleep"
wake_pattern = r"\[\d{4}\-\d{2}\-\d{2} \d{2}:(\d{2})\] wakes up"

sleeps = {}

for line in lines:
    guard = re.match(guard_pattern, line)
    sleep = re.match(sleep_pattern, line)
    wake = re.match(wake_pattern, line)

    if guard:
        current_guard = int(guard.group(1))
        if current_guard not in sleeps:
            sleeps[current_guard] = {}
    elif sleep:
        sleep_time = int(sleep.group(1))
    elif wake:
        wake_time = int(wake.group(1))
        for m in range(sleep_time, wake_time):
            sleeps[current_guard][m] = sleeps[current_guard].get(m, 0) + 1

sleepiest_guard = None
sleepiest_minute = None
most_sleep = 0

for g in sleeps.keys():
    sleep = sum(sleeps[g].values())
    most_sleep = max(sleep, most_sleep)
    if sleep == most_sleep:
        sleepiest_guard = g

most_sleep = 0
for m in sleeps[sleepiest_guard].keys():
    sleep = sleeps[sleepiest_guard][m]
    most_sleep = max(sleep, most_sleep)
    if sleep == most_sleep:
        sleepiest_minute = m

part1 = sleepiest_guard * sleepiest_minute

sleepiest_guard = None
sleepiest_minute = None
most_sleep = 0

for g in sleeps.keys():
    for m in sleeps[g].keys():
        most_sleep = max(sleeps[g][m], most_sleep)
        if sleeps[g][m] == most_sleep:
            sleepiest_guard = g
            sleepiest_minute = m

part2 = sleepiest_guard * sleepiest_minute


print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
