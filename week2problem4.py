import time

    
def missing(arr):
    for i in range(len(arr)):
        if(i==len(arr)-1):
            return "NO ELEMENT MISSED"
        if(int(arr[i+1])-int(arr[i])!=(1)):
            return int(arr[i])+1
    
arr=list(input().split())
firstMissed = missing(arr)
print(firstMissed)

