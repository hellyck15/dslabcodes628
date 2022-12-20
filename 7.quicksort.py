arr = []
n = int(input("enter number of elements:"))
for i in range(0, n):
    ele = int(input("enter ele"))
    arr.append(ele)
print(arr)


def QuickSort(arr):
    elements = len(arr)

    if elements < 2:
        return arr

    current_position = 0

    for i in range(1, elements):
        if arr[i] <= arr[0]:
            current_position += 1
            temp = arr[i]
            arr[i] = arr[current_position]
            arr[current_position] = temp

    temp = arr[0]
    arr[0] = arr[current_position]
    arr[current_position] = temp

    left = QuickSort(arr[0:current_position])
    right = QuickSort(arr[current_position + 1:elements])

    arr = left + [arr[current_position]] + right

    return arr


QuickSort(arr)
print(arr)