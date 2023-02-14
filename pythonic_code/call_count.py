from collections import defaultdict


class CallCount:

    def __init__(self):
        self._counts = defaultdict(int)

    def __call__(self, arg):
        self._counts[arg] += 1
        return self._counts[arg]


cc = CallCount()

print(f"{1}: {cc(1)}")
print(f"{2}: {cc(2)}")
print(f"{2}: {cc(2)}")
print(f"{1}: {cc(1)}")
print(f"{1}: {cc(1)}")
print(f"{'James'}: {cc('James')}")
print(f"{'James'}: {cc('James')}")
print(f"{'Hans'}: {cc('Hans')}")
