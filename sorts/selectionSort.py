def selectionSort(numbers: list) -> int:
    comparaisons = 0
    lowest = 0
    for x in range(len(numbers)):
        lowest = x
        for y in range(x + 1, len(numbers)):
            if numbers[lowest] > numbers[y]:
                lowest = y
            comparaisons += 1
        numbers[x] = numbers[lowest]
        numbers[lowest] = numbers[x]
    return comparaisons
