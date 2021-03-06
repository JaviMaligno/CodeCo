# Biathlon

The first event you are competing in is the Biathlon. It's an event that requires both endurance and precision under stress.

The biathlon event consists of sections of skiing, interspersed with sections of shooting. In each shooting section, you fire 5 shots at 5 targets. You must take a lap on the penalty track for every shot missed before starting to race towards the next section.

You are given the track, which is an array of positive integers, representing the length of each section in meters. There are always at least 2 sections. You are also given the length of the penalty track. It's the same for all shooting sections.

You have a list of your competitors to beat. Your team has compiled some statistics about them, like speed and accuracy. It should help you identify which of them you need to watch out for during the event.

You are given the list of competitors that you have data for as an array of comma-separated values. It has 3 parts, the number on the competitor ski-suit (a unique positive integer), their average speed in m/s (a positive decimal) and their shooting accuracy (a positive integer, at least 2).

For our purposes, shooting accuracy means that that competitor will always miss every n-th shot. So if it's 3, that competitor will always hit twice and miss once, in that order.

You trust your team to give you sensible data, in the right format.

Calculate which competitors would win the event. Return their suit numbers in an array of integers. If there is a tie, order them in increasing order by suit number.

## Example
As an example, given a track made up of these sections `[1000, 3000, 8400, 800, 5000]`, a penalty lap of `600` and given the following competitors, the race would look like this:
```
"1,7.2,5",
"2,6.8,8"
```
- After the first skiing section, competitor 1 is in the lead.
- In the first shooting section, competitor 1 misses 1 shot, while competitor 2 hits all 5. As a result competitor 2 overtakes competitor 1.
- After the second skiing section, competitor 2 remains in the lead.
- In the second shooting section, both competitors miss 1 shot and take a penalty lap, so the standings don't change.
- During the third skiing section, competitor 1 overtakes competitor 2.
- During the third shooting section, competitor 1 misses their last shot again, and during their penalty lap competitor 2 is in the lead again, having not missed a single shot this time.
- In the fourth skiing section, competitor 2 retains their lead but competitor 1 is closing the distance.
- In the fourth shooting section both competitors miss 1, and during the penalty lap competitor 1 gets closer again to competitor 2.
- In the final skiing section competitor, 1 gets very close, but in the end competitor 2 is awarded the gold medal.