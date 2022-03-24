class Slalom:

    def total_displacement(self, offsets, width):
        # Your code goes here

        return self.compute_displacement(width, offsets=offsets, center=0)

    def compute_displacement(self, width, offsets, center):
        gates = len(offsets)
        if gates == 0:
            return 0
        # can be made more efficients because some conditions are redundant, but it's ok
        gate = offsets[0]
        half_width = width / 2
        corners = (gate - half_width, gate + half_width)
        closest_corner = corners[0] if abs(center - corners[0]) < abs(center - corners[1]) else corners[1]
        new_center = center if abs(gate - center) < half_width else closest_corner
        distance = 0 if abs(gate - center) < half_width else min(abs(center - corners[0]), abs(center - corners[1]))
        displacement = distance + self.compute_displacement(width, offsets=offsets[1:], center=new_center)
        return round(displacement, 4)
