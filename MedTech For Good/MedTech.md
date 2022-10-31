# Medical Imaging

The use of computer vision in medical imaging has huge potential not only in advancing the accuracy and reliability of medical procedures that often guide life-changing decisions, but they also have the potential to make the work of medical professionals easier and better.

Although often aided by machine learning, simple pattern matching is also hugely useful in analysing visual samples.

In this challenge, you need to develop a pattern-matching algorithm for 2D scan results. These images are encoded as arrays of ascii strings, where all rows have the same number of characters.

The pattern that you need to match is also an array of ascii strings, similarly with equal-length rows. You can assume at least 1 row, at least 1 character per row for both. Also, the pattern will not have more rows or columns than the image.

You need to find the number of times the pattern is in the scan result. The pattern-matches even if rotated by a multiple of 90 degrees, but it doesn't match if mirrored. It only matches, if all characters are the same within a given region the size of the pattern.

Notably, the same pattern cannot match the exact same area multiple times even if rotated, but pattern-matches can overlap.

For example, this pattern can be found in 3 different places in the scan result (highlighted in green):

```
"x ",
"xx"
```     

<pre>
<code>
" xx    x ",
"  <span style="color:green"> xx  </span>  ",
"   <span style="color:green"> x x </span> ",
"   <span style="color:green">x  xx </span>",
" x<span style="color:green">xx </span>    "
</code>
</pre>

And in this example, the pattern can only be found once (where you can rotate the pattern in one place):

```
" * ",
"***",
" * "
```    
<pre>
<code>
"         ",
"  <span style="color:green">  * </span> **",
"  *<span style="color:green">*** </span>  ",
"   <span style="color:green"> *  </span>  ",
"   ***   "
</code>
</pre>
    