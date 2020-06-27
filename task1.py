# TASK FIVE: HIGHER ORDER FUNCTIONS, GENERATORS, LIST COMPREHENSION AND DECORATOR

# 1. 	 Write a program to Python find the values which is not divisible 3 but is should be a multiple of 7. Make sure to use only higher order function.


def myfunc(lim):
    print("The numbers which are not divisible by 3 but are a multiple of 7 in the given range are: ")
    for i in range (1,lim+1):
        if(i%3!=0 and i%7==0):
            print(i)

def limits():
    upper=int(input("Enter the upper range:"))
    return upper

myfunc(limits())




# 2. 	Write a program in Python to multiple the element of list by itself using a traditional function and pass the function to map to complete the operation.

def multiply(number): 
    return number * number
  
elements = (1, 2, 3, 4,5,6,7,8,9) 
result = map(multiply, elements) 
print(list(result))


# 3. 	Write a program to Python find out the character in a string which is uppercase using list comprehension.

mystring = str(input("Enter the string:"))
  
print("This is the original string : " + mystring) 
  
upperstring = [i for i in mystring if i.isupper()]
  
print("The characters in uppercase in the provided string are: " + str(upperstring)) 



# 4. 	Write a program to construct a dictionary from the two lists containing the names of students and their corresponding subjects. The dictionary should maps the students with their respective subjects. Let’s see how to do this using for loops and dictionary comprehension. HINT-Use Zip function also
# ● Student = [&#39;Smit&#39;, &#39;Jaya&#39;, &#39;Rayyan&#39;]
# ● capital = [&#39;CSE&#39;, &#39;Networking&#39;, &#39;Operating System&#39;]

Students = ["Smith", "Jaya", "Rayyan"] 
Subjects = ["CSE", "Networking", "Operating Systems"] 
   
print ("Name of the students are : " + str(Students)) 
print ("List of the Subjects are : " + str(Subjects)) 
  
result1 = {Students[i]: Subjects[i] for i in range(len(Students))} 
print ("The dictionary with students and their corresponding subjects using  for loop and dictionary comprehension is: " +  str(result1)) 
result2 = dict(zip(Students, Subjects))
print ("The dictionary with students and their corresponding subjects using zip function is : " +  str(result2)) 



# 5. Learn More about Yield, next and Generators


#generator function

def genfunc():
    a=1
    print("First Statement")
    yield a
    
    a+=1
    print("Secind Statement")
    yield a

    a+=1
    print("Third Statement")
    yield a

#for loop 

for item in genfunc():
    print(item)


#initializing list 
list =[2,4,6,8,10]
x= (a**2 for a in list)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
#next(x)


# 6. 	Write a program in Python using generators to reverse the string. Input String = “Consultadd Training”


def revstr(mystring):
    length = len(mystring)
    for i in range(length - 1, -1, -1):
        yield mystring[i]


for i in revstr("Consultadd Training"):
    print(i)



# 7. 	Write any example on decorators.

def gymworkout(func):
    def inner(a, b):
        print("I am going to the gym", a, "and", b)
        if b == 0:
            print("Closed because of COVID19 curfew")
            return

        return func(a, b)
    return inner


@gymworkout
def divide(a, b):
    print(a/b)

divide(10,2)
divide(5,0)

# 8. 	Write a program to handle an error if the user entered the number more than
# four digits it should return “Please length is too short/long !!! Please provide only four
# digits”

while True:
    try:
        x = input("Enter a number consisting of 4 digits: ")
        l=len(x)
       
        if l==4:   
            print("Awesome!! you have entered a 4 digit number.")
            break
        else:
            raise ValueError
    except ValueError as err:
        print("Please length is too short/long !!! please provide only four digits")

 


# 9. 	Create a login page backend to ask user to enter the UserEmail and password.
# Make sure to ask Re-Type Password and if the password is incorrect give chance to
# enter it again but it should not be more than 3 times.

print("Please Enter your UserEmail and Password")
count=1
while count <=3:
    userEmail= input("Enter Your UserEmail: ")
    password = input("Enter Your password: ")
    if userEmail=="User" and password=="password":
        print("Access granted")
        break
    else:
        print("Wrong UserEmail or Password. Try again!")
        count += 1

# 10. 	https://www.programiz.com/python-programming/exception-handling Go
# through this link to understand Finally and Raise concept.
