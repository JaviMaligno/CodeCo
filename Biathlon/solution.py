# from collections import defaultdict
from operator import itemgetter


class Biathlon:

    def find_winners(self, track, miss_penalty, competitors):
        # Your code goes here
        winners = []
        if not competitors:
            return winners

        distance = sum(track)
        tracks = len(track) - 1  # there are shootings only in between, not at the beginning or the end
        shoots = tracks * 5
        splitted = [x.split(",") for x in competitors]
        numbers = [[int(x[0]), float(x[1]), int(x[2])] for x in splitted]
        # times = defaultdict(int) better create a list of tuples
        times = []
        for y in numbers:
            laps = shoots // y[2] #the number of laps they have to take is one for each failed shot, this is the number of failed shots in total
            penalty = laps * miss_penalty
            total_distance = distance + penalty
            time = total_distance / y[1]
            # times[y[0]] = time
            times.append((y[0], time))

        sorted_times = sorted(times, key=(itemgetter(1, 0)))

        min_time = sorted_times[0][1]

        t = min_time
        i = 0
        while t == min_time:
            winners.append(sorted_times[i][0])
            i += 1
            t = sorted_times[i][1] if i < len(sorted_times) else -1

        return winners

