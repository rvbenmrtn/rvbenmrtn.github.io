---
layout: post
title: Counting All Tuples
comments: true
---

In math, the positive integers `1, 2, 3, 4, ...` are the quintessential [countable set](https://en.wikipedia.org/wiki/Countable_set). To show that a set is countable you have to pair up its elements with the positive integers without missing anything. Otherwise it is [uncountable](https://en.wikipedia.org/wiki/Uncountable_set) like the [real numbers](https://en.wikipedia.org/wiki/Real_number).

For example, the positive *even* integers `2, 4, 6, 8, ...` have a natural pairing with the positive integers where you simply double them: `1: 2, 2: 4, 3: 6, 4: 8, ...`. Therefore, the positive even integers are countable.

What's interesting is that pairs (2-[tuples](https://en.wikipedia.org/wiki/Tuple)) of positive integers like `(1,1)` or `(2,3)` are also countable. A way to show this is to treat each pair as an `(x,y)` point and draw a continuous zig-zag over the grid of them, starting at `(1,1)`:

```text
y\x   1     2     3     4     5
1   (1,1) (2,1)-(3,1) (4,1)-(5,1)
      |  /     /     /     /
2   (1,2) (2,2) (3,2) (4,2) 
         /     /     /
3   (1,3) (2,3) (3,3)
      |  /     /
4   (1,4) (2,4)
         /
5   (1,5)
      |...
```

So, following the `|/-` lines, we have pairing `1: (1,1), 2: (1,2), 3: (2,1), 4: (3,1), ...`. The [classic proof](https://www.homeschoolmath.net/teaching/rational-numbers-countable.php) that [rational numbers](https://en.wikipedia.org/wiki/Rational_number) (fractions) are countable follows from this.

Now what's *really* interesting is that you could replace the  sequence of positive integers (`1, 2, 3, ...`) with any other countable sequence, say the sequence of 2-tuples just described.
