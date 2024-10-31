def quickSort(numbers: list) -> int:
    comparaisons = 0
    leftList = []
    rightList = []
    if (len(numbers) <= 1):
        return (0)
    pivotPoint = numbers[0]
    for index in range(1, len(numbers)):
        comparaisons += 1
        if numbers[index] < pivotPoint:
            leftList.append(numbers[index])
        else:
            rightList.append(numbers[index])
    return (comparaisons + quickSort(leftList) + quickSort(rightList))
