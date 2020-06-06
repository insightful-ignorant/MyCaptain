# To calculate fibonacci series of n numbers 

n = int(input("Enter the value of n: "))
if(n<1):
  print("Invalid! Enter a positive integer.")

#first term is zero 
a = 0
#second term is one
b = 1
#third term is addition of previous two terms which is zero initially
sum = 0 
#count to calculate the iterations 
count = 0

print("Fibonacci series: ", end = " ")
while(count<n):
  print(sum, end = " ")
  a = b
  b = sum
  sum = a + b
  count += 1
