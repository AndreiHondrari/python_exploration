#!python3

# type: ignore

from itertools import (
    count, dropwhile, groupby, filterfalse, islice, starmap, tee, takewhile,
    cycle, zip_longest, product, permutations, combinations,
    combinations_with_replacement
)

print("### count")
c = count(step=5)

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print("### cycle")
cy = cycle([2, 5])

print(next(cy))
print(next(cy))
print("repeat from cycle saved from this point")
print(next(cy))  # -> repeat from cycle saved from this point
print(next(cy))

print("### dropwhile")
myitbl = [1, 2, 11, 3, 4]


def fp(x: int) -> bool:
    return x < 10


dw = dropwhile(fp, myitbl)


for x in dw:
    print(x)  # -> drops 1 and 2 (all elements before 11)


print("### group by")
for y in groupby([3, 3, 3, 2, 5, 5, 6, 6, 6, 8]):
    print(y)
    print(y[0])

    # x[1] -> this is a itertools._grouper object
    # (it's an iterator having the complete set)
    for i in y[1]:
        print("-> " + str(i))


print("### filterfalse")
fi = filterfalse(lambda x: x > 3, [1, 3, 4, 10, 1, 2, 8, 1, 4])
print(list(fi))

print("### islice")
si = islice('ABCDEFGHIJKLMNOPQRSTUVXYZ', 2, 10, 3)
print(list(si))

print("### map")
mapped = map(
    lambda x, y, z: x+y+z, (1, 2, 3, 4), (10, 20, 30), (100, 200, 300, 400)
)
print(list(mapped))

print("### starmap")


def totalsum(*args):
    return sum(args)


smp = starmap(totalsum, [[1, 2, 3], [10, 10, 10, 1000, 9]])
print(next(smp))
print(next(smp))

print("### takewhile")
tw = takewhile(lambda x: x < 4, [1, 2, 3, 2, 1, 3, 10, 3, 2, 1, 2, 3, 2, 1])
print(list(tw))

print("### tee")
# splits iterator into n
te = tee([3, 4], 3)

for z in te:
    print(list(z))

print("### zip")
zi = zip([1, 2, 3], [10, 20, 30, 40], [333, 444, 555])
print(list(zi))

print("### zip_longest")
zi = zip_longest(
    [1, 2, 3], [10, 20, 30, 40, 50, 60, 70], [333, 444, 555],
    fillvalue=9999999
)
print(list(zi))

print("### product")
print(list(product([1, 2], [3, 4], [5])))

print("### permutations")
print(list(permutations('ABC', 3)))

print("### combinations")
print(list(combinations('ABC', 2)))
print(list(combinations('ABC', 3)))

print("### combinations_with_replacement")
print(list(combinations_with_replacement('ABC', 3)))
