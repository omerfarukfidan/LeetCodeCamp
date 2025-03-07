"""



"""


def findMinimumDays(durations):
    day_counter = 0
    left, right = 0, 1

    durations.sort(reverse = True)

    while right < len(durations):
        day_counter += 1
        if durations[left] + durations[right] <= 3.00 and len(durations) > 2:
            durations.pop(left)
            durations.pop(right)
        else:
            durations.pop(left)

    if len(durations) == 1 and day_counter == 0:
        return 1
    return day_counter



durations = [1.90, 1.10, 3.00, 2,98, 1.00]
#durations = [1.90, 1.04, 1.25, 2.5, 1.75]
print(findMinimumDays(durations))
