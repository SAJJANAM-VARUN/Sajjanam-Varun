#*****************using recursive func*********
def replacement(num,count):
    if(num==1):
        return count
    else:
        if(num%2==0):
            num=num/2
            count+=1
        else:
            num=num-1
            count+=1
        return replacement(num,count) #recursive function
    
num=int(input())
count=0
print(replacement(num,count))
#*****************using loop**************
"""num=int(input())
count=0
while(num!=1):
    if(num%2==0):
        num=num/2
        count+=1
    else:
    
        num=num-1
        count+=1
print(count)

"""
