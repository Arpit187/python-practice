# Print your name and age ;
print("Name = Arpit Sandhu")
print("Age= 20")
# Add two numbers
a=3
b=5
print("Sum",a+b)
#check weather a number is even or odd
c=int(input("enter the number : "))
if c%2==0:
    print("The number is even")
else:
    print("the number is odd")
#Find the greater of the two numbers

d=int(input("Enter the d number"))
e=int(input("Enter the e  number"))
if d>e:
    print("D is the greater number : ",d)
else:
    print("E is greater number :",e)
#Print the number between the 1 to 10;
for i in range(1,11):
    print(i)
# Print mulitplication of the number
j=3
for i in range(1,11):
    print(j*i)
# find the sum of the numbers from 1 to N
n=int(input("enter the number"))
total=0
for i in range(1,n+1):
    total+=i
    i+=1

print(total)
# count the characters in the string
word="Python"
count=len(word)
print("the total characters in the string :",count)
# reverse the string
print("reverse of the string :",word[::-1])
# find the largest in the list
number=[1,23,34,56,77]
print("the largest elements in the list are : ",max(list(number)))
# create  the function to add the two numbers
def add(a,b):
    sum=a+b
    return sum

a1=add(4,5)
print(a1)
# calculate the total marks and the percentage of a student
def marks(english,Maths,Python,Science):
    totalmarks=english+Maths+Python+Science
    percentage=totalmarks/400*100
    return percentage,totalmarks


m1=marks(78,88,87,98)
print(m1)

    
     