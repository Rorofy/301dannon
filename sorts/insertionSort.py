def insertionSort(numbers: list) -> int:
    comparaisons = 0
    for x in range(1, len(numbers)):
        for y in range(0, x):
            comparaisons += 1
            if (numbers[x] < numbers[y]):
                numbers.insert(y, numbers[x])
                numbers.pop(x + 1)
                break
    return comparaisons
