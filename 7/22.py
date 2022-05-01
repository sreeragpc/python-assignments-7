""" Write a program to add the values of two 2D arrays
Program should contains 3 functions including the main function
main()
Call function getArray()
Call function addArray()
Call function displayArray()
		getArray()
Get values to the array
		getArray()
Add array 1 and array 2
		displayArray()
Display the array values
"""

def getarray(l,d):
    #size = int(input("enter the size of array"))
    size=d
    print("enter the elements of array : ")
    for i in range(size):
      m=[]
      for j in range(size):
        m.append(int(input()))
      l.append(m)
    return l

def addarray(q,w,d):
    #size = int(input("enter the size of array"))
    size=d
    l3=[]
    for i in range(size):
      m3=[]
      for j in range(size):
        m3.append(0)
      l3.append(m3)
    for i in range(size):
        for j in range(size):
            l3[i][j]=q[i][j]+w[i][j]
    return l3

def displayarray(k):
        print("sum = " + str(k))
def main():
    n = int(input("enter the size of array : "))
    arr1 = []
    arr2=[]
    l1 = getarray(arr1,n)
    l2=getarray(arr2,n)
    z=addarray(l1,l2,n)
    displayarray(z)
main()
