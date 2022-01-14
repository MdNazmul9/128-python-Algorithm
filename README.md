# 128-python-Algorithm
##### The inputs to the problems are called instances.
#### Accepted
Accepted Your program provides the correct output in the allotted time. Congrat-
ulations!

#### Presentation Error
Presentation Error Your program is almost accepted, but the output contains
extraneous or missing blanks or end-of-lines. This message occurs rarely.

#### Compilation Error
Compilation Error The compilation of your program generates errors. Often,
clicking on this message will provide the nature of the error. Be sure to compare
the version of the compiler used by the judge with your own.

#### Wrong Answer
Wrong Answer Re-read the problem statement, a detail must have been over-
looked. Are you sure to have tested all the limit cases? Might you have left
debugging statements in your code?

#### Time Limit Exceeded
Time Limit Exceeded You have probably not implemented the most efficient
algorithm for this problem, or perhaps have an infinite loop somewhere. Test
your loop invariants to ensure loop termination. Generate a large input instance
and test locally the performance of your code.

#### Runtime Error
Runtime Error In general, this could be a division by zero, an access beyond the
limits of an array, or a pop() on an empty stack. However, other situations can
also generate this message, such as the use of assert in Java, which is often not
accepted.
#### join
```
‘-’.join([’A’,’B’,’C’])  returns the string “A-B-C” .

```
#### Container
The principal complex data structures are dictionaries, sets, lists and n-tuples. These
structures are called containers

### List
```
The following expressions have a complexity linear in the length of L, with
the exception of the first, which is in constant time.
L[i]  the i th element of L
L[i:j] the list of elements with indices starting at i and up to (but not including) j
L[:j] the first j elements
L[i:] all the elements from the i th onwards
L[-3:] the last three elements of L
L[i:j:k] elements from the i th up to (but not including) the j th, taking only every k th element
L[::2] the elements of L with even indices
L[::-1] a reverse copy of L

The most important methods of a list for our usage are listed below. Their
complexity is expressed in terms of n, the length of the list L . A function has
constant amortised complexity if, for several successive calls to it, the average
complexity is constant, even if some of these calls take a time linear in n.

len(L) -- returns the number of elements of the list L -- O(1)
sorted(L) -- returns a sorted copy of the list L -- O(n log n)
L.sort() -- sorts L in place -- O(n log n)
L.count(c)-- the number of occurrences of c in L -- O(n)
c in L -- is the element c found in L ? -- O(n)
L.append(c) -- append c to the end of L -- amortised O(1)
L.pop() -- extracts and returns the last element of L -- amortised O(1)

```
