#program asks for input and converts to integer
#program takes integer and generates sequence of numbers, starting at 1,2,3
#program prints 1,2,3
#sequence is then generated from the last 3 numbers of sequence

n = int(input("Enter the length of the sequence: ")) # Do not change this line

num1 = 1
num2 = 2
num3 = 3

print(num1)
print(num2)
print(num3)

for i in range(n-3):
    sum = num1+num2+num3
    num1 = num2
    num2 = num3
    num3 = sum
    print(sum)   
