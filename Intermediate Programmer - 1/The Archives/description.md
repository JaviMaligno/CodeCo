# Challenge description

You are working as a researcher in the Archives, a vast collection of knowledge stored physically and encoded digitally with signifier codes.

The signifier codes are represented in the format `0-00-000000-0`.

You have been approached by a detective. She needs to prove the innocence of their client, who is sentenced to death on April 26th.

The client claims to have been framed and that there is a note hidden in a book stored within the Archives will prove it.

Finding the book should be easy - Each code is ten digits long and the last number (known as a check digit) is used to verify the identity of the document.

There is a problem however:

Someone has been covering their tracks. Someone has changed the check digit on every document in this section of the Archives.

Luckily, being an experienced researcher, you know that the check digit is determined by taking the sum of each digit multiplied by its integer weight (1-9 in ascending order) modulo 11.

For example, to calculate the check digit (`x`) for `0-19-852663-x` you would use the equation $((0\times 1)+(1\times 2)+(9\times 3)+(8\times 4)+(5\times 5)+(2\times 6)+(6\times 7)+(6\times 8)+(3\times 9)) \mod 11$.

You can simply write a method to determine the check digit when provided with a representation of the signifier code, e.g. `0-19-852663-x`, where `x` represents the check digit.

If the input is not in a valid format return $-1$.

You can use this method to find any document in this section of the Archives, and so you can find the book!

Hurry though, the the life of the detective's client depends on you.
