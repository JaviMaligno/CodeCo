# Challenge description

Pascal's triangle is a triangular array of binomial coefficients. The triangle starts with a row *n* = 0 containing a single element 1. The elements of each proceeding row are calculated by adding the above-left and above-right array elements treating empty values as 0.

The total for the layer *n* can be considered as the sum of each element in the specific layer of Pascal's triangle.

Write a method to calculate the *nth* layer total of Pascal's triangle. Your solution should accept a positive integer value and return an integer result representing the layer total. In the event that you are unable to return a valid integer result then **-1** should be returned.
