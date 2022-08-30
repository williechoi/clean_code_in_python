test_list = [1, 3, 5, 7, 9, 11, 13, 17, 18, 20, 22]

even_number = next(
    (
        i
        for i in test_list
        if i % 2 == 0
    ), None
)

print(even_number)
