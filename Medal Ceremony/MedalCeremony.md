# Challenge description

At the end of all the competitions, it's time for the medal ceremonies! Fortunately to you, you won quite a few medals. And a large number of journalists are also here to talk to you about your performance. You're not even sure you have time for all of them.

You are given a list of locations where medals will be awarded, and the times when the ceremonies will be. They are in the following format: `x,y,hh:mm`, where `x` and `y` are integer coordinates of the location of the ceremony, and `hh:mm` are the start time of the ceremony. Each ceremony lasts 45 minutes after the start. After the ceremony you need to go to the next location. It takes euclidian distance minutes to move between locations.

The input will always be a valid schedule, with sensible coordinates, valid times, events in the correct order, on the same day, with enough time to go between them.

You also want to give as many interviews between these ceremonies as possible. Interviews are done at the news building located at `0,0`. Each interview lasts 15 minutes. To do interviews, you have to go to the news building, do as many consequtive interviews as possible and then go to the next scheduled award ceremony.

Calculate how many interviews you can hold between all the award ceremonies. Return the count as an integer.

## Example
Let's consider an example:
```
"-12,4,8:56",
"3,-3,11:06",
"-11,3,12:21",
"-5,10,13:16",
```
Between the first two ceremonies, it would take `16.55` minutes to travel between the two locations, but you have 85 minutes between the two, so you can make it to the news building in `12.65` minutes, give 4 interviews, and then go to the next location in `4.24` minutes, just in time for the next ceremony.

Next, you have 30 minutes between the two ceremonies, so although you can get to the news building in `4.24` minutes and then to the next location from there in `11.40` minutes, that doesn't leave enough time to do a full interview, so you have to go to the next location directly.

Finally, between the third and fourth locations, you only have 10 minutes between the ceremonies, so you just barely make it there (as the direct journey lasts `9.22` minutes).

As a result, in total you gave `4` interviews between the ceremonies, so you should return that value.