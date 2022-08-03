# mappedrange.py
import logging

logger = logging.getLogger()


class MappedRange:
    """Apply a transformation to a range of numbers."""

    def __init__(self, transformation, start, end):
        self._transformation = transformation
        self._wrapped = range(start, end)

    def __getitem__(self, index):
        value = self._wrapped.__getitem__(index)
        result = self._transformation(value)
        logger.info("Index %d: %s", index, result)
        return result

    def __len__(self):
        return len(self._wrapped)


if __name__ == '__main__':
    mr = MappedRange(abs, -10, 5)
    print(mr[0])
    print(mr[-1])
    print(list(mr))
    
