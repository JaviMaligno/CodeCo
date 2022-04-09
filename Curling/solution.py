from math import sqrt, log, exp


class Curling:
    d = 1
    f = 0.05

    def push_stones(self, v1, y1, v2, y2):
        # Your code goes here
        f = Curling.f
        # (hypothetical) stopping distance
        x1 = v1 / f
        x2 = v2 / f
        if self.collision(x1, x2, y1, y2):
            x1, y1, x2, y2 = self.collide(x1, y1, v2, y2)
            return self.qualified(x1, x2, y1, y2)
        else:
            return self.qualified(x1, x2, y1, y2)

    def collision(self, x1, x2, y1, y2):
        d = Curling.d
        # if the offsets are too different, they won't collide
        if abs(y1 - y2) >= d:
            return False
        # case 1: x2 is too short to collide
        elif x2 <= x1 - d:
            return False
        # case 2: they surely collide
        elif x2 >= x1:
            return True
        # case 3: x2 is in the range of the first stone
        else:
            return (x1 - x2) ** 2 + (y1 - y2) ** 2 < d
        # maybe return 0,1,2 to distinguish the cases and not having to check again
        # I probably don't need that because I can compute where the collision happens

    def qualified(self, x1, x2, y1, y2):
        d = Curling.d
        r = d / 2
        condx1 = x1 > 35 - r or x1 < 25 + r
        condx2 = x2 > 35 - r or x2 < 25 + r
        condy1 = y1 > 5 - r or y1 < -5 + r
        condy2 = y2 > 5 - r or y2 < -5 + r

        if condx1 or condy1:
            if condy2 or condx2:
                return -1
            else:
                return round(sqrt((30 - x2) ** 2 + y2 ** 2), 2)
        else:
            if condy2 or condx2:
                return round(sqrt((30 - x1) ** 2 + y1 ** 2), 2)
            else:
                d1 = sqrt((30 - x1) ** 2 + y1 ** 2)
                d2 = sqrt((30 - x2) ** 2 + y2 ** 2)
                return round(min(d1, d2), 2)

    def collide(self, x1, y1, v2, y2):
        d = Curling.d
        f = Curling.f
        # in the moment of collision there is a right triangle with hypotenuse d=1 and one side abs(y1-y1)
        # The other side is given by
        side1 = abs(y1 - y2)
        side2 = sqrt((d ** 2 - side1 ** 2))
        x2 = x1 - side2
        # After the collision, analogue movements start, we just need to compute the extra distance
        # and then with the angle we get the new coordinates
        angle_sine = side1 / d  # opposite side divided by hypotenuse d = 1
        angle_cosine = side2 / d

        t = -log(1 - x2 * f / v2)/f  #time of collision
        v2 = exp(-f * t) * v2  #speed at collision
        v1 = v2 * angle_cosine

        s1 = v1 / f
        x1 = x1 + s1 * angle_cosine
        y1 = y1 + s1 * angle_sine if y2 < y1 else y1 - s1 * angle_sine

        # this one moves perpendicularly, i.e. cosine and sine will be used to compute the opposite coordinate
        v2 = v2 * angle_sine
        s2 = v2 / f
        x2 = x2 + s2 * angle_sine
        y2 = y2 + s2 * angle_cosine if y1 < y2 else y2 - s2 * angle_cosine

        return x1, y1, x2, y2


#if __name__ == '__main__':
 #   solution = Curling()
  #  print(solution.push_stones(1.5, 0, 1.8, 0.707))
