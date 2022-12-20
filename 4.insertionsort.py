arr = []
n = int(input("enter number of elements:"))
for i in range(0, n):
    ele = int(input("enter ele"))
    arr.append(ele)
print(arr)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key


insertion_sort(arr)
print(arr)