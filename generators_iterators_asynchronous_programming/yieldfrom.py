
def all_powers(n, pw):
    yield from (n**i for i in range(pw+1))


for v in all_powers(2, 3):
    print(v)
