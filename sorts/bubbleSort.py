def bubbleSort(numbers: list) -> int:
    comparaisons = 0
    iterations = 0
    value = 0
    rvalue = 0
    while True:
        for index in range(len(numbers) - 1 - iterations):
            value = numbers[index]
            rvalue = numbers[index + 1]
            if rvalue < value:
                numbers[index] = rvalue
                numbers[index + 1] = value
            comparaisons += 1
        if iterations == len(numbers) - 1:
            break
        iterations += 1
    return comparaisons
