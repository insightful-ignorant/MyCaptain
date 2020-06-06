mixed_list = [10, 9, 8, -7, 6, -5, 4, 3]

print('Before: ',mixed_list)

for num in mixed_list:
  if(num < 0):
    mixed_list.remove(num)
   
print("After: ",mixed_list)
