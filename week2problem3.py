#method 1

def occurance(arr,key):
    count=0
    for i in arr:
        if(i==str(key)):
            count+=1
    return count

arr=input().split()
key=int(input())

occ=occurance(arr,key)
print(occ)


"""
#************using inbuilt count funtion************* 
#method 2

def occurance(arr,key):
    return arr.count(str(key))
        
arr=input().split()
key=int(input())

occ=occurance(arr,key)
print(occ)

"""
