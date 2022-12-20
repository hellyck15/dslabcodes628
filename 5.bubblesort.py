arr = []
n = int(input("enter number of elements:"))
for i in range(0, n):
    ele = int(input("enter ele"))
    arr.append(ele)
print(arr)


def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp


bubble_sort(arr)
print(arr)
