arr = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input("enter ele"))
    arr.append(ele)
print(arr)


def linear_Search(arr, n, key):
    for i in range(0, len(arr)):
        if (arr[i] == key):
            return i
    return -1


key = int(input("enter the element you want to search "))

res = linear_Search(arr, len(arr), key)

if (res == -1):
    print("Element not found")
else:
    print("Element found at index: ", res)