#MAXIMUM ITEM IN ARRAY
'''a = int(input("enter the number of arrsy="))
t =list(map(int,input("enter the elements of array=").strip().split()))
print(t)
s = (max(t))
print(s)'''

#REVERSE THE ARRAY
'''a=int(input("Number of elements in the array:-"))
n=list(map(int, input("elements of array:-").strip().split()))
print(n[: : -1])'''

#FLOYD'S TRIANGLE
'''n = 5
number = 1
for i in range (1,n+1):
    for j in range(1,i+1):
        print(number, end =' ')
        number=number+1
    print()'''
#PATTERN
'''n1= int(input("enter the number of line for pattern"))
for i in range(1,n1+1):
    for j in range(1,i+1):
        print('*',end ='')
    print()'''
 #DIVISIBILITY OF 7 AND 5 
'''n3= 100

for i in range(1,n3+1):
    if i%35==0:
        print(i)
        i=i+1'''

#GRADING SYSTEM
'''nums = int(input("enter your numbers to know your grade"))
if nums>=90:
    print ("your grade is A+")
elif nums==80:
    print("your grade is B+")
elif nums==60:
    print("your grade is c")
else:
    print("do hardwark your grade is below average")'''

#PRINTING CHARACTERS IN PATTERN (EQUILATERAL TRIANGLE)
'''print("equilateral triangle pattern by using characters")
size = 7
asciiNumber = 65
m = (2*size)-2
for i in range(0,size):
    for j in range(0,m):
        print(end=" ")
    m =m-1
    for j in range (0,i+1):
        character = chr(asciiNumber)
        print(character,end=' ')
        asciiNumber +=1
    print(" ")
'''
#FIRST NON REPEAING ELEMENT
def first_non(arr, n):
    for i in range(n):
        j=0
        while(j<n):
            if( i!=j and arr[i] ==arr[j]):
                break
            j+=1
        if j==n:
            return[i]
    return -1

arr = [9,3,4,53,5,4]
n=len(arr)
print(first_non(arr,n))

    