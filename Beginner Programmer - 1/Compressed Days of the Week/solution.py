class Solution:

    def compress_days(self, input_days):
        # Your code goes here
        week = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
        order = dict(zip(week, range(7)))
        sorted_days = sorted(input_days, key = lambda x: order[x])
        short_days = "".join(map(lambda x: x[0],sorted_days))
        if short_days == "MTWTF":
            output = "D"
        elif short_days == "SS":
            output = "E"
        elif short_days == "SMTWTFS":
            output = "A"
        else:
            output = short_days
        return output