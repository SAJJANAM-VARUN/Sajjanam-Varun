def zerOne(num,index):
    prev_row='0' #initialising with 0 at the begining
    row="" #empty string 

    if(num==1 and index==1):
        return 0 

    while(num!=1):
        row="" 
        for ele in prev_row:
        
            if(ele=='0'):
                row=row+'01'
                
            else:
                row=row+'10'

        prev_row=row  #storing a copy of present string for next iteration
        num-=1
    
    return prev_row[index-1]

num=int(input())
index=int(input())
result=zerOne(num,index)
print(result)
