def sum_every_second(numbers, index):
    if index >= len(numbers):
        return 0
    if numbers == []:
        return "FALSEEE"
    return numbers[index] + sum_every_second(numbers, index + 2)

print(sum_every_second([1, 2, 3, 4, 5], 2))