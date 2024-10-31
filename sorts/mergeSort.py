def mergeSort(numbers: list) -> int:
    comparaisons = 0
    if (len(numbers) <= 1):
        return(0)
    leftList = numbers[len(numbers) // 2:]
    rightList = numbers[:len(numbers) // 2]
    leftSubList = mergeSort(leftList)
    rightSubList = mergeSort(rightList)
    while len(leftList) != 0 and len(rightList) != 0:
        if (leftList[0] < rightList[0]):
            numbers[comparaisons] = leftList.pop(0)
        else:
            numbers[comparaisons] = rightList.pop(0)
        comparaisons += 1
    if len(leftList) != 0:
        for i in range(comparaisons, len(numbers)):
            numbers[i] = leftList.pop(0)
    if len(rightList) != 0:
        for i in range(comparaisons, len(numbers)):
            numbers[i] = rightList.pop(0)
    return comparaisons + leftSubList + rightSubList
