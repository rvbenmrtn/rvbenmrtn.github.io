---
layout: post
title: Counting All Tuples
comments: true
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

The crucial point now is that this could be repeated again! Replace y with the sequence of 3-tuples and we get countable 4-tuples. Do it again for countable 5-tuples. For any non-negative integer n, the set of n-tuples of positive integers is countable!

I never actually mentioned 0-tuples or 1-tuples but there is only one 0-tuple `()` and the sequence for 1-tuples `(1), (2), (3), (4),...` is obvious.

Finally, what's amazing is you can show that *all* n-tuples combined are countable. Let `Tn_k` define the kth n-tuple and arrange each countable sequence of n-tuples on a column of the grid:

```text
k\n   1    2    3    4    5
1    T1_1 T2_1 T3_1 T4_1 ...

2    T1_2 T2_2 T3_2 T4_2

3    T1_3 T2_3 T3_3 T4_3 

4    T1_4 T2_4 T3_4 T4_4

5    ...
```

Then list off the diagonals like before for a countable sequence of all n-tuples for all positive n: `T1_1, T2_1, T1_2, T3_1, T2_2, T1_3, T4_1, ...` (the same `(x,y)` pattern 2-tuples had but it's `(n,k)`). This works out to `(1), (1,1), (2), (1,1,1), (2,1), (3), (1,1,1,1), ...` respectively pairing with `1, 2, 3, 4, 5, 6, 7, ...`.

Thus the combination of infinitely many infinite sets is in fact countable!

## Coding It

