#function to rotate array by d element

def rotateArray(arr,n,d):
    temp = []
    i =0
    while (i<d):
        temp.append(arr[i])
        i = i+1
    i=0
    while(d<n):
        arr[i]=arr[d]
        i=i+1
        d=d+1
    arr[:] = arr[:i]+temp
    return arr

#Driver function to test above function
arr = [1,2,3,4,5,6,7]
print("Array after left rotation is:",end='')
print(rotateArray(arr,len(arr),2))


#Function to left rotate arr[] of size n by d*/

def leftRotate(arr,d,n):
    for i in range(d):
        leftRotatebyOne(arr,n)

#Function to left Rotate arr[] of size n 1*/
def leftRotatebyOne(arr,n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp
#Utility function to print an array

def printArray(arr,size):
    for i in range(size):
        print("%d"% arr[i],end=" ")

#Driver program to test above function

arr = [1,2,3,4,5,6,7]
leftRotate(arr,2,7)
printArray(arr,7)


#Function to left rotate arr[] of size n by d
def leftRotate(arr,d,n):
    for i in range(gcd(d,n)):
        temp = arr[i]
        j = i
        while 1:
            k = j+d
            if k>=n:
                k = k-n
            if k==i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp

def printArray(arr,size):
    for i in range(size):
        print("%d" % arr[i],end='')
def gcd(a,b):
    if b==0:
        return a;
    else:
        return gcd(b,a%b)

#Driver program to test above funtions
arr = [1,2,3,4,5,6,7]
leftRotate(arr,2,7)
printArray(arr,7)


#Python program using the List
#slicing approch to rotate the array

def rotateList(arr,d,n):
    arr[:] = arr[d:n]+arr[0:d]
    return arr
#Driver function to test above function
arr = [1,2,3,4,5,6,7]
print(arr)
print("Rotate list is")
print(rotateList(arr,2,len(arr)))
                                    
