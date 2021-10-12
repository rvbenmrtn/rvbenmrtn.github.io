from itertools import islice


def cantor_pairing(k1, k2):
    return (k1 + k2) * (k1 + k2 + 1) // 2 + k2


def xy_pairing(x, y):
    return cantor_pairing(x - 1, y - 1) + 1


print(xy_pairing(1, 1))  # -> 1
print(xy_pairing(2, 1))  # -> 2
print(xy_pairing(1, 2))  # -> 3
print(xy_pairing(3, 1))  # -> 4


def zero_tuples():
    """Finite generator over all 0-tuples, namely ()."""
    yield ()


print(list(zero_tuples()))  # -> [()]


def one_tuples(start=1):
    """Infinite generator over all 1-tuples (start+k,) for k=0,1,2,3,..."""
    while True:
        yield start,
        start += 1


for _, t in zip(range(5), one_tuples()):
    print(t, end=' ')  # -> (1,) (2,) (3,) (4,) (5,)
print()

print(list(islice(one_tuples(), 5)))  # -> [(1,), (2,), (3,), (4,), (5,)]


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


for _, t in zip(range(5), combine(one_tuples(), one_tuples())):
    print(t, end=' ')  # -> (1, 1) (2, 1) (1, 2) (3, 1) (2, 2)
print()


def n_tuples(n):
    """Returns generator over n-tuples of positive integers for int n > 0."""
    return one_tuples() if n == 1 else combine(one_tuples(), n_tuples(n-1))


def n_tuples_iterative(n):
    """Returns generator over n-tuples of positive integers for int n > 0."""
    generator = one_tuples()
    for _ in range(n - 1):
        generator = combine(one_tuples(), generator)
    return generator


for _, t in zip(range(5), n_tuples(3)):
    print(t, end=' ')  # -> (1, 1, 1) (2, 1, 1) (1, 2, 1) (3, 1, 1) (2, 2, 1)
print()


def all_tuples():
    """Infinite generator over all n-tuples of positive integers for all n."""
    yield from zero_tuples()
    lists, generators = [], []
    diagonal = 1
    while True:
        for y_index in range(diagonal):
            x_index = diagonal - y_index - 1
            if x_index == len(lists):
                generators.append(n_tuples(diagonal))
                lists.append([])
            if y_index == len(lists[x_index]):
                lists[x_index].append(next(generators[x_index]))
            yield lists[x_index][y_index]
        diagonal += 1


def print_all_tuples(stop_at=99):
    places = len(str(stop_at))
    for i, t in zip(range(stop_at + 1), all_tuples()):
        print(f"{i:>{places}} ({','.join(map(str, t))})")


print_all_tuples(15)


# from contextlib import redirect_stdout
# with open('tuples.txt', 'w') as f, redirect_stdout(f):
#     print_all_tuples(10000)
