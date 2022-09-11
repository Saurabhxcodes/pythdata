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
    print(n3, end = " ")
print()
'''
# Find Repeated character in String
'''str = 'barabanki'
for i in str:
    count = 0
    for j in str:
        if i==j:
            count+=1
        if count>1:
            break

    if count==1:
        print(i,end =" ")'''
        

        
        






