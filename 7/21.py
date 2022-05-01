""" Write a program to multiply the adjacent values of an array and store it in an another array
Program should accept an array
Multiply the adjacent values
Store the result into another array
"""

size=int(input("enter the size of array"))
list=[]
print("enter the elements of array 1")
for i in range(size):
    element=int(input())
    list.append(element)
print("list = "+str(list))
list2=[]
for j  in range(size):
   if (j+1)<size:
    tempfile=list[j]*list[j+1]
    list2.append(tempfile)
print("array after multipication"+str(list2))



