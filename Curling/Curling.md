# Curling

The final event of the competition is the most exciting: Curling.

In this competition, teams slide curling stones towards a target area. For us to have a fighting chance, we need to simulate where the stones will land after our push.

The core physics of curling is fairly straightforward. The stone is released at the start line travelling with some initial velocity. Due to friction, as time passes they travel slower until they come to a stop. During this time, it has travelled some distance. We can calculate momentary speed (the magnitude of the velocity) like this `v = exp(-f * t) * v0`, where `f` is the coefficient of friction, `t` is time and `v0` is the initial speed. Calculating its integral to get the distance travelled after the same `t` time we get `s = v0 / f * (1 - exp(-f * t))`.

We draw two axes on the ice: the X-axis is along the length of the ice and the Y-axis is perpendicular to it. Each stone is pushed parallel to the X-axis at some distance from the centre. The target is on the X-axis, 30 meters from the starting line.

Using these, we can calculate the first two pushes in a game (one from each team). If during the second push the stones collide, we model this the following way:

- Take the vector pointing from the position of the second stone at the moment of collision to the position of the first stone.
- The first stone will move along this vector, and its speed will be the speed of the second stone at the moment of collision, multiplied by the cosine of the angle between the vector and the X-axis.
- The second stone will move perpendicular to this vector, and its speed will be its speed at the moment of collision, multiplied by the sine of the angle between the vector and the X-axis.

Points are awarded to the team with the closest stone to the target. However, stones that are outside or even partially outside the area around the target are disqualified. The area is 10m wide and starts at 25m to 35m from the starting line.

You are given the starting speed (in m/s) and starting offset along the Y-axis (in m) of both of the two stones. The coefficient of friction `f` on ice is `0.05`. The diameter of the stones is 1m. Calculate the distance between the target and the closest stone in meters. Round to 2 decimal places. If both stones have been disqualified, return `-1`.
For the purposes of this simulation, ignore the effects of sweeping or the spinning motion of the stones.

## Examples
Let's consider some examples:

The first stone starts with a speed of 1.6 m/s at offset -0.6 m. It slides for 32 meters before stopping.

The second stone is pushed with a speed of 1.4 m/s at an offset of 1.8 m. It slides for 28 meters before stopping.

Because the two don't collide, the first stone will be closer to the centre (2.09 m compared to 2.69 m).

Here is a second example:

The first stone starts with a speed of 1.5 m/s at an offset of 0 m. It slides for 30 meters before stopping.

The second stone starts with a speed of 1.8 m/s at an offset of 0.707 m. It collides with the first stone at `t = 33.607 s`. At this point, it has travelled 29.293 m and its current speed is 0.335 m/s. The angle of the vector pointing from the second stone through the first is 45 degrees with the X-axis.

Following the collision, the first stone travels with `v = cos(45) * 0.335 = 0.237 m/s` along the axis of collision and stops at (33.355, -3.354). The second stone travels with `v = sin(45) * 0.335 = 0.237 m/s` perpendicular to the axis of collision and stops at (32.645, 4.061).

The first stone is closer to the target (4.74 m compared to 4.85 m).

And one last example:

The first stone starts with a speed of 1.8 m/s at an offset of 0 m. It slides for 36 meters before stopping.

The second stone starts with a speed of 1.75 m/s at an offset of 0.5 m. It slides for 35 meters before stopping.

As both stones are outside the box around the area around the target, they are both disqualified, and you should return `-1`.