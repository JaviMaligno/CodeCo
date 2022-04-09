# Figure skating

The third event in this competition is Figure Skating. Coordination and elegance all wrapped up into a sport.

You have already completed your routine. It went well, not counting the two times you fell face first.

The judges are doing the scoring, but it seems like the score calculation is still done by hand afterwards. If you could get a glance at the scorecards you could know the score before it's announced.

You manage to take some pictures, but now you need to calculate the actual score. Scoring is done the following way:

- A panel of judges each assign a set of points to each performance.
- The scoring has two halves: Technical score and program score.
- In the technical scoring section, each element of your routine is assigned a standard score (you know these) and then each judge scores it between -5 and 5, in 0.25 increments. The highest and lowest values are removed (in the case of a duplicate, only one value is removed), then the scores are averaged and are added to the base score.
- In the program score section, each judge assigns a score for the overall performance in 4 categories between 0.25 and 10 in 0.25 increments. Similarly, the highest and lowest values are removed and averaged to give the final score.
- The total score is given as a sum of technical and program scores.

A judge scorecard is a string of decimal numbers separated by commas `,`. However, they have some problems.

- If the number is not in a 0.25 increment, you should round it to the nearest 0.25.
- If a number is not within the allowed range for the section, ignore it.
- Also, if a scorecard has the wrong number of values, ignore the entire scorecard.
- Finally, if for an element/performance scoring you are not able to remove the highest and lowest values (because you only have 1 or 2 values), average all numbers. If you don't have any values for an element, don't modify the base score in the technical section and give 5 in the program section.

Your inputs are all the scorecards you managed to gather and the base scores for the elements you performed (you can assume that these are correct). You should return the total score, rounded to 4 decimal places.

## Examples

Consider these examples:

Scorecards:
```
"1.25,-5,2.5,8.5,6.25,0.25,10",
"2.5,-4.75,1.75,7.75,6.5,0.75,9.5",
"2,-5,2.25,8.25,6.0,0.5,9.5"
```           
Base scores:
```
[5, 4.25, 2]
```
The scores with the remaining values highlighted and averages calculated, combined with the base scores:
<pre><code>
1.25, <b>2</b>, 2.5 => 2 + 5 = 7
-5, <b>-5</b>, -4.75 => -5 + 4.25 = -0.75
1.75, <b>2.25</b>, 2.5 => 2.25 + 2 = 4.25
7.75, <b>8.25</b>, 8.5 => 8.25
6.0, <b>6.25</b>, 6.5 => 6.25
0.25, <b>0.5</b>, 0.75 => 0.5
9.5, <b>9.5</b>, 10.0 => 9.5
</code></pre>
Which adds up to a total score of `35.0`.

Here is another example:

Scorecards:
```
"-5.5,1.5,-0.75,-1.5,3.75,1.5,8.0,4.5,5.0",
"-4.5,2.5,-1.25,-2.75,3.25,1.75,9.25,3.75,7.75",
"-3.75,-0.25,0.25,-4.0,5.25,0.25,8.5,3.0,6.0",
"-5.0,0.75,-0.75,0.0,3.75,1.5,10.0,2.25,6.0",
"-4.5,1.25,-2.0,-1.0,5.75,0.25,10.0,4.5,10.25",
```
Base scores:
```
[7.25, 4.75, 5.25, 4.0, 1.25]
```
From the rounded scores the ones not eliminated are highlighted and averages calculated, combined with the base scores:
<pre><code>
<del>-5.5</del>, -5, <b>-4.5, -4.5</b>, -3.75 => -4.5 + 7.25 = 2.75
-0.25, <b>0.75, 1.25, 1.5</b>, 2.5 => 1.6667 + 4.75 = 5.9167
-2.0, <b>-1.25, -0.75, -0.75</b>, 0.25 => -0.9167 + 5.25 = 4.3333
-4.0, <b>-2.75, -1.5, -1.0</b>, 0.0 => -1.75 + 4.0 = 2.25
3.25, <b>3.75</b>, 3.75, <del>5.25</del>, <del>5.75</del> = 3.75 + 1.25 = 5
0.25, <b>0.25, 1.5, 1.5</b>, 1.75 => 1.0833
8.0, <b>8.5, 9.25, 10.0</b>, 10.0 => 9.25
2.25, <b>3.0, 3.75, 4.5</b>, 4.5 => 3.75
5.0, <b>6.0, 6.0,</b> 7.75, <del>10.25</del> => 6.0
</code></pre>
Which adds up to a total score of `40.3333`.