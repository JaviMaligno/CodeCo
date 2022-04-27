from datetime import datetime
from math import sqrt


class MedalCeremony:

    def count_possible_interviews(self, ceremonies):
        # Your code goes here
        ceremonies = [x.split(",") for x in ceremonies]
        FMT = "%H:%M"
        ceremonies = [[(int(x[0]), int(x[1])), datetime.strptime(x[2], FMT)] for x in ceremonies]
        return self.recursion(ceremonies)

    def distance(self, a):
        return sqrt(a[0] ** 2 + a[1] ** 2)

    def compute_time(self, start, second):
        time1 = self.distance(start[0])
        time2 = self.distance(second[0])
        total = time1 + time2

        time3 = (second[1] - start[1]).total_seconds() / 60 - 45
        d = time3 - total
        return 0 if d < 0 else int(d / 15)

    def recursion(self, ceremonies):
        if len(ceremonies) <= 1:
            return 0
        number = self.compute_time(ceremonies[0], ceremonies[1])
        return number + self.recursion(ceremonies[1:])
