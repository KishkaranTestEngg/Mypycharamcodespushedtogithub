
# name="hello world"
# normal order
# print(name[::-1]) # [start:stop:step] 1 position
# print(name[::2]) # [start:stop:step] 2 position
# print(name[::])
# print(name[4]) # print o
#print(name[4:9]) # print o and r start and stop means -1 (ex) 9 means -1
# print(name[4:11])

# reverse order
# print(name[::-1]) # [start:stop:step] 1 position
# print(name[-1::-6])
# name = 'hello world' # d=-1, l=-2, r=-3, o=-4, w=-5,space='6' ----
# # print(name[-1::-1]) # [start:stop:step] # -1:you can skip writing stop : you cannot skip step part, -1 + 1 = 0
# # print(name[-1:-4:-1]) # -1, -1 + -1 = -2, -2+-1 = -3
# print(name[-2:-9:-2]) # -2 (l), -2+-2 = -4 (o), -4 + -2 = -6(space), -6 + -2 = -8
# # print(name[::-2])

# String slicing concept

# String slicing in Python means extracting a part (substring) of a string using index positions.

# name="Venkatakishore"  # Slice from index 0 to 6  and index pos start from 0 means v here
# print(name[0:8])

# name="venkatakishore" # Slice from index 1 to 5
# # print(name[1:5])
#
# # print(name[::]) # it gives the full string value
#
# print(name[::-1]) #used to print the string in reverse order

def sum(a, b):
    return a + b

result = sum(2, 3)
print(result)



