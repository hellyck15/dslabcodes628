arr=[]
n= int(input("enter number of elements:"))
for i in range(0,n):
    ele = int(input("enter ele"))
    arr.append(ele)
print(arr)

def selection_sort(arr,l):
    for i in range(l):
        minpos = i
        for j in range(i+1,l):
            if arr[j]<arr[minpos]:
                minpos = j
        (arr[i],arr[minpos])=(arr[minpos],arr[i])

selection_sort(arr,len(arr))
print(arr)