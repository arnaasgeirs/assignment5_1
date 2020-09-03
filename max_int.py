
#1 Program asks for an input, converts to integer 
#2 Program checks if integer is a positive number. If negative, then program goes to the end, step 5
#3 While input is positive, program goes back to step 1, asking for input. 
#4 Program compares all integers and finds the maximum integer
#5 Program runs until input is a negative number, then halts. 


num_int = int(input("Input a number: "))    # Do not change this line
max_int = 0
while num_int >= 0:
    if num_int >= max_int:
        max_int = num_int
    num_int = int(input("Input a number: ")) 

print("The maximum is", max_int)    # Do not change this line
