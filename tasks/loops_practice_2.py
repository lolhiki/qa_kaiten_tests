numbers = list(range(1, 10))
max_number = numbers[0]

for i in numbers:
    if i > max_number:
        max_number = i

    if i == 9:
        break

print(max_number)
