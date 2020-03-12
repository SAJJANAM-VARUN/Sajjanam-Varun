num=int(input())
arr=[]
for i in range(0,num+1):
    num_bin=bin(i)[2:] # Binary conv of a number
    freq=num_bin.count('1') #returns no.of 1's in given string
    arr.append(freq)
print(arr)
    
