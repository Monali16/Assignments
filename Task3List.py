#TASK THREE: DATA STRUCTURES 

#1. Create a list of the 10 elements of four different types of Data Type like int, string, complex and float. 

listint = [0,1,2,3,4,5,6,7,8,9]
print(listint)

liststring = ['white', 'black', 'red','pink','purple','blue','orange','green', 'yellow', 'violet']
print(liststring)

listcomplex = ['3i', '1+3j', '1+4j', '3j', '5i', '5j','6i','6j','7i','7j' ]
print(listcomplex)

listfloat = [1.3,1.4,1.5,1.6,1.7,1.8,1.9,1.10,1.11,1.12]
print(listfloat)



#2. Create a list of size 5 and execute the slicing structure.  

m=list(range(5))
print(m[:])

#3. Write a program to get the sum and multiply of all the items in a given list.

x = [1,3,5,7,9]
print(sum(x))

x = [1,3,5,7,9]
for i in range(len(x)):
    x[i] = x[i]*3
    print(x)

#4. Find the largest and smallest number from a given list. 
y= [10,20,30,40,50,60]
print(max(y))
print(min(y))

#5. Create a new list which contains the specified numbers after removing the even numbers from a predefined list.  
z = [1,2,3,4,7,9,10,11,13,16]

for i in z:
    if(i%2==0):
        z.remove(i)
        print(z)


#6. Create a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included). 
l = []

for i in range(1,31):
    print(i**2)

print(l[0:5])
print(l[25:31])


#7. Write a program to replace the last element in a list with another list. 

#Sample data: [[1,3,5,7,9,10],[2,4,6,8]] 

#Expected output: [1,3,5,7,9,2,4,6,8] 

m = [1,3,5,7,9,10]
n= [2,4,6,8]
print(m[-1])
m[-1:]=n
print(m)

 
 