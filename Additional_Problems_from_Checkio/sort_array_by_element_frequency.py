"""
https://py.checkio.org/en/mission/sort-array-by-element-frequency/
"""


def frequency_sort(items):
    freqDict, rsltList, refList = {}, [], []

    # Calculate frequency and collect unique item to reference list.
    for item in items:
        if item in freqDict:
            freqDict[item] += 1
        else:
            freqDict[item] = 1
            refList.append(item)

    # Use bubble sort to sort refList by item frequency in descending order.
    for i in range(len(refList)):
        for j in range(i + 1, len(refList)):
            if freqDict[refList[i]] < freqDict[refList[j]]:
                temp = refList[i]
                refList[i] = refList[j]
                refList[j] = temp

    # Calculate result list.
    for item in refList:
        rsltList += [item for _ in range(freqDict[item])]

    return rsltList


print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))
