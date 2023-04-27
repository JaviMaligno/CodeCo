# Challenge Description


You are the manager of a restaurant. And not just any restaurant.
A *fancy* restaurant.

Your problem is that your restaurant is so popular that you have a limited supply of ingredients, and so you decide to limit the choices people can make when ordering from your menu.
You will be provided a list of `N` integers, where `N` is the number of courses and each integer is the number of dishes for that course on the menu. These contstraints will be provided as a list of strings in one of two forms, either `A.B+C.D `or `A.B-C.D `, where `A.B `refers to dish `B` from course `A`, and similarly for `C.D`. A , B, C, D are valid 0-indexed integers and A must be different to C. A + indicates that if dish  `A.B `is picked, then `C.D `must also be picked, and - indicates that if `A.B `is picked then `C.D` cannot be picked.

You should return the total number of possible choices where one dish is picked from each course obeying the contraints.
