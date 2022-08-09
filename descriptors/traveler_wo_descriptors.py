# traveler w/o descriptors

class Traveler:

    def __init__(self, name, current_city):
        self.name = name
        self._current_city = current_city
        self._cities_visited = [current_city]

    @property
    def current_city(self):
        return self._current_city

    @current_city.setter
    def current_city(self, new_city):
        if new_city != self._current_city:
            self._cities_visited.append(new_city)

        self._current_city = new_city

    @property
    def cities_visited(self):
        return self._cities_visited


alice = Traveler("Alice", "Barcelona")
alice.current_city = "Paris"
alice.current_city = "Brussels"
alice.current_city = "Amsterdam"

print(alice.cities_visited)
