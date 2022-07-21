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

n=int(input("Number of elements in the array:-"))
arr=list(map(int, input("elements of array:-").strip().split()))
print(arr)
for(int i=0; i<n; i++){
    if arr[i]=arr[n-1]{
        print("duplicate is present")
    else:
        print("no duplicate")
    }

}
