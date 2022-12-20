arr = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input("enter ele"))
    arr.append(ele)
print(arr)


def binary_search(arr, l, h, key):
    if h >= l:
        mid = l + (h - l) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search(arr, mid - 1, l, key)
        elif arr[mid] < key:
            return binary_search(arr, mid + 1, h, key)
    else:
        return -1


key = int(input("enter the element you want to search"))
res = binary_search(arr, 0, len(arr), key)

if (res == -1):
    print("element not found")
else:
    print("element found at", res)