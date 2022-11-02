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
'''def first_non(arr, n):
    for i in range(n):
        j=0
        while(j<n):
            if( i!=j and arr[i] ==arr[j]):
                break
            j+=1
        if j==n:
            return[i]
    return -1

arr = [9,9,4,53,5,4,53]
n=len(arr)
print(first_non(arr,n))'''


'''arr = list(map(int,input("enter the elements").split()))
print("you have entered these elements",arr)
print("the maximum number in the array is",max(arr))
print("the minimum number in the array is",min(arr))'''

'''class cars:
    def __init__(self,color,modal,year,speed):
        self.color=color
        self.modal=modal
        self.year=year
        self.speed=speed
tata  = cars('black','harrier',2000,140)
print(tata.modal)
print (tata.__dict__)'''


'''def is_palindrome(s):
    left_pos = 0
    right_pos = len(s)-1

    while right_pos>=left_pos:
        if not s[left_pos]==s[right_pos]:
            return False
        left_pos +=1
        right_pos -=1
    return True
print(is_palindrome("aza")) '''


'''def total_food(r,arr,unit,n):
    if n==0:
        return -1
    totalfoodReq = unit*r
    foodtillNow=0
    house = 0

    for house in range(n):
        foodtillNow+=arr[house]
        if foodtillNow>=totalfoodReq:
            break
    if totalfoodReq>foodtillNow:
        return 0 
    return house+1
r= int(input("enter r"))
unit =int(input("enter unit of r"))
n = int(input("enter number of houses"))
arr = list(map(int,input("enter the arr").split()))   
print(total_food(r,unit,n,arr)) '''

'''def binary_operations(str):
    a = int(str[0])
    i=1
    while i<len(str):
        if str[i]=='A':
            a&=int(str[i+1])
        elif str[i]=='B':
            a|=int(str[i+1])
        else:
             a^=int(str[i+1])
        i+=2
    return a
str = input()
print(binary_operations(str))'''

#PASSWORD CHECKER


'''def pass_checker(str,n):

    if n<4:
        return 0
    if str[0].isdigit():
        return 0
    cap = 0
    num = 0
    for i in range(n):
        if str[i]==' ' or str[i]=='/':
            return 0
        if str[i]=='A' and str[i]<='Z':
            cap+=1
        elif str[i].isdigit():
            num+=1
    if cap>0 and num>0:
        return 1 
    else:
        return 0
str = input()
a = len(str)
print(pass_checker(str,a)) '''


'''

n = int(input())
m = int(input())
s = 0
d = 0
for i in range(1,m+1):
    if i %n==0:
        s+=i
    else:
        d+=i    
print(abs(d-s)) '''


#large small sum 

'''n = int(input())
arr = list(map(int,input().split()))
odd_arr = []
even_arr = []
for i in range(n):
    if i%2==0:
        even_arr.append(arr[i])
    else:
        odd_arr.append(arr[i])
odd_arr=sorted(odd_arr)
even_arr =sorted(even_arr)
print(odd_arr[1] + even_arr[1])'''

'''n = int(input())
arr = list(map(int,input().split()))
sum = int(input())
t=[]
if n<2:
    print("error")
arr = sorted(arr)
for i in range(n-1):
    if arr[i]+arr[i+1]<=sum:
        print(arr[i]*arr[i+1])
        break
    else:
        print("0")'''

'''def solution(n,arr):
    t =[]
    
    arr = sorted(arr)

    for i in range(n):
        if (arr[i]-arr[i+1]==1):
            arr=arr.remove(arr[i+1])
            t.append(arr[i])
        
        return arr
n = int(input("enter the no of arrays"))
arr =list(map(int,input().split()))
print(solution(n,arr))'''

'''
list1 = list(map(int,input("\nEnter the numbers : ").split()))
list2 = list(map(int,input("\nEnter the numbers : ").split()))
list3 = []
for i in range(len(list1)):
    if list1[i]>0:
        list3.append(list1[i])   
for j in range(len(list2)):
    if list2[i]>0:
        list3.append(list2[i])  


print(list3)
list3 = sorted(list3)
print(list3)
'''
'''def increments(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if(char.isupper()):
            result+=chr((ord(char)+s-65) % 26 + 65)
        else:
            result +=chr((ord(char)+s-97) % 26 + 97)
    return result
text = "Hello"
s = 4
print("text:",text)
print("shift:" +str(s))
print("cipher" + increments(text,s))'''

#sum of array

'''def sum(arr):
    sum =0
    for i in arr:
        sum = sum +i
    return sum 
arr = list(map(int,input("enter the array").split()))
print(sum(arr))'''
        

#largest element of array

'''def larArr(arr):
    t = sorted(arr)
    return t[-1]
arr = list(map(int,input("enter the array==").split()))
print(larArr(arr))'''

#swap first and last element of the list
'''def swap(arr):
    t= arr[0]
    arr[0]=arr[-1]
    arr[-1]=t
    return arr
arr = list(map(int,input("enter the elements of list").split()))
print(swap(arr))'''

#find length and element presence in the list

'''def findL(arr,d):
    for i in range(len(arr)):
        if arr[i]==d:
            return True
        else:
            s="element not present"
            return s
            
arr = list(map(int,input("enter the elements of list==>").split()))
d = int(input("enter the ele to search=="))
print(findL(arr,d))'''


class Sports_veh:
    def __init__(self):
        self.name = ""
        self.noOfVehicle = ""
        self.vehicle1 = ""
        self.vehicle2 = ""

    def setPersonDetails(self, newName, noOfVehicle, vehicle1, vehicle2):
        self.name = newName
        self.noOfVehicle = noOfVehicle
        self.vehicle1 = vehicle1
        self.vehicle2 = vehicle2

    def getPersonDetails(self):
        print(self.name, "has", self.noOfVehicle, "vehicle one is",
              self.vehicle1, "and another is", self.vehicle2)


class vehicle:
    def __init__(self):
        self.fuel = ""
        self.uses = ""
        self.operation = ""


class hondaAccordCar(vehicle):
    def sethondaAccordCar(self, newfuel, uses, madein):
        self.fuel = newfuel
        self.uses = uses
        self.operation = madein

    def getHondaAccordCar(self):
        print("Honda accord car runs on fuel called", self.fuel)
        print("Honda accord is", self.uses, "and", self.operation)


class DucatiBike(vehicle):
    def setDucatiBike(self, newFuel, uses, imported):
        self.fuel = newFuel
        self.uses = uses
        self.operation = imported

    def getDucatiBike(self):
        print("Ducati runs on fuel called", self.fuel)
        print("Ducati is", self.uses, "and", self.operation, "vehicle")


if __name__ == "__main__":
    p = Sports_veh()
    p.setPersonDetails("Sourabh", "two", "honda accord car", "Ducati Bike")
    p.getPersonDetails()
    


   
    d = DucatiBike()
    d.setDucatiBike("petrol", "used", "imported")
    d.getDucatiBike()

    h = hondaAccordCar()
    h.sethondaAccordCar("diesel", "new", "made in india")
    h.getHondaAccordCar()
   

   
        





        














































    














                     
