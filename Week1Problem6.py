def single_occurance(input_arr):
    for num in input_arr:
        if(input_arr.count(num)==1): # counts the freq of the number specified and checks if it occurs 1
            return num
        
input_arr=input().split()
print(single_occurance(input_arr))
        
    
