from datetime import timedelta, date


class DateRangeContainerIterable:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def __iter__(self):
        current_day = self.start_date
        while current_day < self.end_date:
            yield current_day
            current_day += timedelta(days=1)


class DateRangeIterable:
    """An iterable that contains its own iterator object"""

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    def __iter__(self):
        return self

    def __next__(self):
        if self._present_day >= self.end_date:
            raise StopIteration

        today = self._present_day
        self._present_day += timedelta(days=1)
        return today


class WebPageUrlIterable:
    """An iterable that contains its own iterator object"""
    url = 'https://www.navajo.org/bbs/board?page=%d'

    def __init__(self, start_index, end_index):
        self.start_index = start_index
        self.end_index = end_index
        self._current_index = start_index

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_index >= self.end_index:
            raise StopIteration

        index = self._current_index
        self._current_index += 1
        return self.url % index


for day in DateRangeIterable(date(2018, 1, 1), date(2018, 1, 5)):
    print(day)

for day in DateRangeContainerIterable(date(2018, 1, 1), date(2018, 1, 5)):
    print(day)


