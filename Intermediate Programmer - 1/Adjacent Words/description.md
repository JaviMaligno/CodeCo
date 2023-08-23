# Challenge description


Given two strings you must determine if they are adjacent and return either true or false.

To determine if the two strings are adjacent we must first determine if the letters in each string are adjacent.

Two letters are adjacent if:

* They are the same letter, or
* They are lexigraphically adjacent, i.e. $J \rightarrow I$, $J \rightarrow K$

  ($Z\rightarrow A$ is NOT adjacent).

Two strings are adjacent if:

* They are the same length, and
* Each letter is adjacent to a unique letter in the other word.

Therefore, for example, the strings $CAT$ and $SAD $ are adjacent as $C \rightarrow D$, $A \rightarrow A$ and $T \rightarrow S$.

For the purpose of the question, you can assume both strings taken as input contain only uppercase characters.
