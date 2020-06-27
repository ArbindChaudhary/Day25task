# TASK: OBJECT ORIENTED
# 1.	Write a program that calculates and prints the value according to the given formula:
# Q= Square root of [(2*C*D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.

import math
C=50
H=30
D=[]
result=[]
Dval=input("Enter the value of D:")
D=Dval.split(",")
D= [int(i)for i in D]
i=0
l=len(D)

while (i<1):
    Q=(math.sqrt((2*C*D[i])/H))
    result.append(Q)
    i+=1
    print("The Squareroot of given value is:", result)




# 2.Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have an area function which can print the area of the shape where Shape’s area is 0 by default.

class Shape():
    def area(self, a,b):
        x= a*b
        print("The area of the given value is:", +x)



class Sqr():
    def __init__(self, length):
        self.length=  length*length    
        print("The square of the given value is:", +self.length)   

S= Shape()
sq=Sqr(3)

S.area(5,10)
sq



# 3.Create a class to find the three elements that sum to zero from a set of n real numbers.
# Input array: [-25,-10,-7,-3,2,4,8,10]
# Output: [[-10,2,8],[-7,-3,10]]

class elements():
    def sumtozero(self, arg, x):
        for i in range(0, x-2):       
            for j in range(i+1, x-1): 
                for k in range(j+1, x): 
                    if (arg[i] + arg[j] + arg[k] == 0): 
                        print("The three elements that sum to zero are:", +arg[i], arg[j], arg[k]) 
El=elements()
arg=[-25,-10,-7,-3,2,4,8,10]
El.sumtozero(arg, len(arg))  


 
# 4.          What is the output of the following code? Explain your answer as well.
# class Test:
#     def __init__(self):
#         self.x = 0
# class Derived_Test(Test):
#     def __init__(self):
#         self.y = 1
# def main():
#     b = Derived_Test()
#     print(b.x,b.y)
# main()

# Answer=> We will get an error as the variables x and y are not defined


 
# class A:
#     def __init__(self, x= 1):
#         self.x = x
# class der(A):
#     def __init__(self,y = 2):
#         super().__init__()
#         self.y = y
# def main():
#     obj = der()
#     print(obj.x, obj.y)
# main())


# Answer=> The output will be 1  2



 
# class A:
#     def __init__(self,x):
#         self.x = x
#     def count(self,x):
#         self.x = self.x+1
# class B(A):
#     def __init__(self, y=0):
#         A.__init__(self, 3)
#         self.y = y
#     def count(self):
#         self.y += 1     
# def main():
#     obj = B()
#     obj.count()
#     print(obj.x, obj.y)
# main()

#Answer=> we will get the ouput as 3  1

 
 
 
# class A:
#     def __init__(self):
#         self.multiply(15)
#         print(self.i)
 
#     def multiply(self, i):
#         self.i = 4 * i;
# class B(A):
#     def __init__(self):
#         super().__init__()
 
#     def multiply(self, i):
#         self.i = 2 * i;
# obj = B()

#Answer=> The output will be 30 




 
# 5.	Create a Time class and initialize it with hours and minutes.
# Make a method addTime which should take two time object and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# Make a method displayTime which should print the time.
# Make a method DisplayMinute which should display the total minutes in the Time. E.g.- (1 hr 2 min) should display 62 minute.

 class Time():

   def __init__(self, hours, mins):
     self.hours = hours
     self.mins = mins

   def addTime(self,t1, t2):
     t3 = Time(0,0)
     if t1.mins+t2.mins > 60:
      t3.hours = (t1.mins+t2.mins)//60
     t3.hours = t3.hours+t1.hours+t2.hours
     t3.mins = (t1.mins + t2.mins) % 60
     return t3

   def displayTime(self):
     print ("Time is",self.hours,"hours and",self.mins,"minutes.")

   def displayMinute(self):
     print ((self.hours*60)+self.mins)

 a = Time(2,40)
 b = Time(1,30)
 c = Time.addTime(a,b)
 c.displayTime()
 c.displayMinute()

# 6.           Write a Person class with an instance variable, , and a constructor that takes an integer, , as a parameter. The constructor must assign  to  after confirming the argument passed as  is not negative; if a negative argument is passed as , the constructor should set  to  and print Age is not valid, setting age to 0.. In addition, you must write the following instance methods:
# yearPasses() should increase the  instance variable by .
# amIOld()  should perform the following conditional actions:
# If , print You are young..
# If  and , print You are a teenager..
# Otherwise, print You are old..	
# Sample Input:
# 4
# -1
# 10
# 16
# 18
# Sample Output:
# Age is not valid, setting age to 0.
# You are young.
# You are young.
 
# You are young.
# You are a teenager.
 
# You are a teenager.
# You are old.
 
# You are old.
# You are old.

class Person:
    def __init__(self,initialAge):
   
        self.initialAge = age
    def amIOld(self):
       
        if age <= 0:
            age is 0
            print("Age is not valid, setting age to 0")

        elif age < 13:
            print("You are young.")

        elif 13 <= age < 18:
            print("You are teenager.")

        else:
            print("You are old.")
    def yearPasses(self):
     
        return age+1
t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")