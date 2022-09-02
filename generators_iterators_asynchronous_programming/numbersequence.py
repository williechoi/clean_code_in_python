# Using iterator
# Iterable Object
class NumberSequence:
    def __init__(self, start=0):
        self.current = start

    def __next__(self):
        current = self.current
        self.current += 1
        return current

    def __iter__(self):
        return self


seq = NumberSequence(10)
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))


# Using generator
# Generator Function
# yield keyword makes function a generator
def sequence(start=0):
    while True:
        yield start
        start += 1


seq = sequence(80)
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))


# relying on flag to signal termination
def search_nested_bad(array, desired_value):
    coords = None
    for i, row in enumerate(array):
        for j, cell in enumerate(row):
            if cell == desired_value:
                coords = (i, j)
                break

        if coords is not None:
            break

    if coords is None:
        raise ValueError(f"{desired_value} not found")

    print("Value %r found at [%i, %i]", desired_value, *coords)
    return coords


def _iterate_array2d(array2d):
    for i, row in enumerate(array2d):
        for j, cell in enumerate(row):
            yield (i, j), cell


def search_nested(array, desired_value):
    try:
        coord = next(
            coord
            for (coord, cell) in _iterate_array2d(array)
            if cell == desired_value
        )
    except StopIteration as e:
        raise ValueError(f"{desired_value} not found") from e

    print("Value %r found at [%i, %i]", desired_value, *coord)
    return coord


# an example of an iterator object that is not iterable
# Since this object did not implement __iter__, it cannot be used in for _ in loop..
class SequenceIterator:
    def __init__(self, start=0, step=1):
        self.current = start
        self.step = step

    def __next__(self):
        value = self.current
        self.current += self.step
        return value


si = SequenceIterator(1, 2)
print(next(si))
print(next(si))
print(next(si))


# for _ in SequenceIterator(): pass -> this code throws error


class MappedRange:
    """Apply a transformation to a range of numbers."""

    def __init__(self, transformation, start, end):
        self._transformation = transformation
        self._wrapped = range(start, end)

    def __getitem__(self, index):
        value = self._wrapped.__getitem__(index)
        result = self._transformation(value)

        print("Index %d: %s" % (index, result))
        return result

    def __len__(self):
        return len(self._wrapped)


mr = MappedRange(abs, -10, 5)
print(mr[0])
print(mr[1])
print(list(mr))
