'''my_str ="themameht"
my_str = my_str.casefold()
rev_str = reversed(my_str)
if list(my_str) == list(rev_str):
    print("the given string is palindrome")
else:
    print("this is not a palindrome") '''

    #ROMAN INTO INTEGER
'''class py_solution:
    def roman_to_int(self,s):
        rom_val={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        int_val= 0 
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]]>rom_val[s[i-1]]:
                int_val+=rom_val[s[i]] -2* rom_val[s[i-1]]
            else:
                int_val +=rom_val[s[i]]
        return int_val
print(py_solution().roman_to_int('MCVI'))'''


#REVERSE THE NUMBER

'''num =int (input("enter the number to get its reverse"))
temp = num 
reverse = 0
while num > 0:
    remainder = num%10
    reverse = (reverse*10)+remainder
    num = num//10
print("the given number is {} and reverse number is {}".format(temp,reverse))'''

#REVERSE THE STRING

'''str1 = input("enter the string for reverse ==")
rev = str1[::-1]
print("The reverse of the string is ==",rev)'''

#Fibonacci series

'''n= int(input("enter the number for fibonacci series"))
n1=0
n2=1
for i in range(2,n):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n1,n2,n3, end = " ")
print()
'''
#ADD THE 2ND LARGEST AMONG EVEN POSITIONED AND SECOND LARGEST AMONG ODD POSITIOND (SUM)
# 
'''def LargeSmallSum(arr, N):
    even_arr = []
    odd_arr = []
    for i in range(N):
        if i%2 ==0:
            even_arr.append(arr[i])
        else:
            odd_arr.append(arr[i])
    even_arr = sorted(even_arr)
    odd_arr = sorted(odd_arr)
    s= even_arr[-2] + odd_arr[-2]
    return s
arr = [3,2,1,7,5,4]
N = len(arr)
print(LargeSmallSum(arr,N)) '''

'''def fiboSum(n):
    if n<=1:
        return n 
    else:
        return(fiboSum(n-1) + fiboSum(n-2))
nterms = 12
m =2
div_sum =[]
t = []
sum = 0

if nterms <=0:
        print("please enter valid no.")
else:
    print("fibo series is")
    for i in range(nterms):
        print(fiboSum(i))
        
        div_sum.append(fiboSum(i))
    print(div_sum)
    for i in range(len(div_sum)):
        if div_sum[i]%m==0:
            t.append(div_sum[i])
    print(t)
    for i in t:
        sum = sum+i
    print(sum)'''

'''def discriminant(a,b,c):
    s=b*b
    t=4*a*c
    results = s-t
    return results
a=3
b=6
c=4
print(discriminant(a,b,c))'''






        
        

    

 

      












        

        
        






