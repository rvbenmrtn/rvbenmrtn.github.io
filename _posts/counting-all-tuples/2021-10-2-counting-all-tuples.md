---
layout: post
title: Counting All Tuples
comments: true
excerpt: Exploring the countability of n-tuples of positive integers and Python code that generates them.
---

In math, the positive integers `1, 2, 3, 4, ...` are the quintessential [countable set](https://en.wikipedia.org/wiki/Countable_set). To show that a set is countable you have to [pair up](https://en.wikipedia.org/wiki/Bijection) its elements with the positive integers without missing anything. Otherwise it is [uncountable](https://en.wikipedia.org/wiki/Uncountable_set) like the [real numbers](https://en.wikipedia.org/wiki/Real_number).

For example, the positive *even* integers `2, 4, 6, 8, ...` are countable because they have a natural pairing with the positive integers : `1→2, 2→4, 3→6, 4→8, ...`.

## [Counting 2-Tuples](#counting-2-tuples)

What's interesting is that ordered pairs (2-[tuples](https://en.wikipedia.org/wiki/Tuple)) of positive integers like `(1,1)` or `(2,3)` are also countable. A way to show this is to treat each pair as an `(x,y)` point and draw successive diagonals down and left from every `(x,1)` point:

```text
y\x   1     2     3     4     5     6
1   (1,1) (2,1) (3,1) (4,1) (5,1)  ...
         /     /     /     / 
2   (1,2) (2,2) (3,2) (4,2)
         /     /     /
3   (1,3) (2,3) (3,3)
         /     /
4   (1,4) (2,4)
         /    
5   (1,5)

6   ...
```

Then list the diagonals from shortest to longest, so the order is `(1,1), (2,1), (1,2), (3,1), (2,2), (1,3), (4,1), ...`, pairing with `1, 2, 3, 4, 5, 6, 7, ...` respectively. This corresponds to a 1-indexed [Cantor pairing function](https://en.wikipedia.org/wiki/Pairing_function#Cantor_pairing_function), which can be implemented in Python as:

```py
def cantor_pairing(k1, k2):
    return (k1 + k2) * (k1 + k2 + 1) // 2 + k2

def xy_pairing(x, y):
    return cantor_pairing(x - 1, y - 1) + 1

print(xy_pairing(1, 1))  # -> 1
print(xy_pairing(2, 1))  # -> 2
print(xy_pairing(1, 2))  # -> 3
print(xy_pairing(3, 1))  # -> 4
```

The [classic proof](https://www.homeschoolmath.net/teaching/rational-numbers-countable.php) that [rational numbers](https://en.wikipedia.org/wiki/Rational_number) are countable follows from this fact that ordered pairs are.

## [Counting N-Tuples](#counting-n-tuples)

Now what's *really* interesting is that you can just view the x or y sequence of positive integers used above as any other countable sequence -- we know they can map to each other after all.

For example, replace y with the sequence of 2-tuples just described and repeat the same `(x,y)` diagonalization:

```text
y\x          1         2         3         4
1=(1,1)   (1,(1,1)) (2,(1,1)) (3,(1,1))  ...
                   /         /         /
2=(2,1)   (1,(2,1)) (2,(2,1)) (3,(2,1))  ...
                   /         /         /
3=(1,2)   (1,(1,2)) (2,(1,2)) (3,(1,2))
                   /         /
4=(3,1)        ...        ...
```

The `(x,y)` pairs start to feel like Lisp-style lists and can be compressed to 3-tuples. So the order goes `(1,1,1), (2,1,1), (1,2,1), (3,1,1), ...` and we have shown  that 3-tuples are countable.

The crucial point now is that this could be repeated again. Replace y with the sequence of 3-tuples and we get countable 4-tuples. Do it again for countable 5-tuples, etc. For any non-negative integer n, the set of n-tuples of positive integers is countable!

(I never actually mentioned 0-tuples or 1-tuples but there is only one 0-tuple `()` and the sequence for 1-tuples `(1), (2), (3), (4),...` is obvious.)

Finally, what's amazing is you can show that all n-tuples for all n combined are countable. Let `Tn_k` be the kth n-tuple and arrange each countable sequence of n-tuples on a column of the grid:

```text
k\n   1    2    3    4    5
1    T1_1 T2_1 T3_1 T4_1 ...

2    T1_2 T2_2 T3_2 T4_2

3    T1_3 T2_3 T3_3 T4_3 

4    T1_4 T2_4 T3_4 T4_4

5    ...
```

Then list off the diagonals like before for a countable sequence of all n-tuples for all positive n: `T1_1, T2_1, T1_2, T3_1, T2_2, T1_3, T4_1, ...` (the same `(x,y)` pattern 2-tuples had but it's `(n,k)`). This works out to `(1), (1,1), (2), (1,1,1), (2,1), (3), (1,1,1,1), ...` pairing with `1, 2, 3, 4, 5, 6, 7, ...` respectively. Tack `0` paired with the empty tuple `()` on the front for the sake of completeness.

Thus a combination of infinitely many infinite sets is in fact countable! This is not always true but works here because the sets are countable and there are countably many of them.

## [Coding It](#coding-it)

The goal now is to write some Python 3 code that actually generates the infinite sequences of n-tuples described above.

### [0-Tuples and 1-Tuples](#0-tuples-and-1-tuples)

It starts off easy with 0-tuples and 1-tuples.

The empty tuple is the only 0-tuple so we can have a generator that [yields](https://www.geeksforgeeks.org/python-yield-keyword/) it and does nothing else:

```py
def zero_tuples():
    """Finite generator over all 0-tuples, namely ()."""
    yield ()

print(list(zero_tuples()))  # -> [()]
```

For 1-tuples we can make an endless generator by repeatedly yielding and incrementing a value:

```py
def one_tuples(start=1):
    """Infinite generator over all 1-tuples (start+k,) for k=0,1,2,3,..."""
    while True:
        yield start,
        start += 1
```

Note the comma in `yield start,` makes it yield a one-element tuple rather than the integer `start`.

Here, since the generator is infinite, `list(one_tuples())` would never finish. But we can zip with a bounded range or take an [iterator slice](https://docs.python.org/3/library/itertools.html#itertools.islice) to see some quick output:

```py
for _, t in zip(range(5), one_tuples()):
    print(t, end=' ')  # -> (1,) (2,) (3,) (4,) (5,)
```

```py
from itertools import islice
print(list(islice(one_tuples(), 5)))  # -> [(1,), (2,), (3,), (4,), (5,)]
```

### [Combining Into N-Tuples](#combining-into-n-tuples)

To make sequences of 2-tuples and beyond we need a way to combine two infinite generators with the diagonalization method described [above](#counting-2-tuples).

The following `combine` function does just that. It maintains two lists corresponding to the elements of the x and y axes of the grid. It generates the lists from the generators as needed with the internal `get_index` function. It carefully indexes the lists in the `for` loop to get the current `(x,y)` that are combined with `combiner`, which by default adds so it concatenates tuples. The entire lists need to be kept in memory since every diagonal references everything in both lists up to that point.

```py
def combine(x_generator, y_generator, combiner=lambda x, y: x + y):
    """Combines two infinite generators into one by arranging them in a grid
       and taking diagonals in the same way as the Cantor pairing function."""
    def get_index(lst, gen, index):
        if index == len(lst):
            lst.append(next(gen))
        return lst[index]
    x_list, y_list = [], []
    diagonal = 1
    while True:
        for y_index in range(diagonal):
            x_index = diagonal - y_index - 1
            x = get_index(x_list, x_generator, x_index)
            y = get_index(y_list, y_generator, y_index)
            yield combiner(x, y)
        diagonal += 1
```

Combining `one_tuples` with itself gives the sequence of 2-tuples we expect:

```py
for _, t in zip(range(5), combine(one_tuples(), one_tuples())):
    print(t, end=' ')  # -> (1, 1) (2, 1) (1, 2) (3, 1) (2, 2)
```

But of course the goal is to be able to produce n-tuple generators for any n. The `n_tuples` function does this recursively in one line by combining `one_tuples()` with the next smaller n-tuple:

```py
def n_tuples(n):
    """Returns generator over n-tuples of positive integers for int n > 0."""
    return one_tuples() if n == 1 else combine(one_tuples(), n_tuples(n-1))
```

An iterative version is also possible:

```py
def n_tuples_iterative(n):
    """Returns generator over n-tuples of positive integers for int n > 0."""
    generator = one_tuples()
    for _ in range(n - 1):
        generator = combine(one_tuples(), generator)
    return generator
```

For n = 3, `n_tuples` generates the sequence of 3-tuples we expect:

```py
for _, t in zip(range(5), n_tuples(3)):
    print(t, end=' ')  # -> (1, 1, 1) (2, 1, 1) (1, 2, 1) (3, 1, 1) (2, 2, 1)
```

### 


bring zero_tuples back in