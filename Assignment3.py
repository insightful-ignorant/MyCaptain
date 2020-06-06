#Assigning elements to different lists
list_num = [1,3,5]
list_word = ['ban', 'can', 'man']
tuple_letters = ('a', 'e', 'i')
list_num.append(tuple_letters)
print(list_num)
list_word.extend(tuple_letters)
print(list_word)
print('\n')

#Accessing elements from a tupl
tuple1 = (10, 20, [30, 40])
print("Original tuple is: ",tuple1)
#Indexing
print(tuple1[2][0])
#Negative Indexing
print(tuple1[-1])
#Slicing
print(tuple1[1:])
print("\n")

#Deleting different dictionary elements
dict = {"Jane":21, "Alex":33, "Ben":25}
print("Original dictionary is: ",dict)
#using del keyword
del dict["Jane"]
print(dict)
#using pop method
value = dict.pop("Alex")
print("The deleted value is",value)
print(dict)
