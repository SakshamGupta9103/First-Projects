# Simple Calculator
# Description: A basic calculator that can handle basic arithmetic operations.
# Skills learned: Functions, error handling, user input validation.
# This Program have two numbers
print("Available operators: +, -, *, /, //, **,  <, >")

operator=input("Enter the select Operator :   ")

num1=int(input("Enter the First Number :  "))
num2=int(input("Enter the Second Number :  "))
while True:
    if operator=="+":
        print("Additional of ",num1,'+',num2 ,'=',num1+num2)
        break
    elif operator=="-":
        print(" Subtraction of ",num1,'-',num2 ,'=',num1-num2)
        break
    elif operator=="*":
        print("Mutiple of ",num1,'*',num2 ,'=',num1*num2)
        break
    elif operator=="/":
        print("Division of ",num1,'/',num2 ,'=',num1/num2, 'Float Division')
        break
    elif operator=="//":
         print("Division of ",num1,'/',num2 ,'=',num1/num2, ' Int Division')
         break
    elif operator=="**":
        print("The Power of ",num1,'**',num2 ,'=',num1**num2)
        break
    elif operator=="<":
        print("Number 1 is lesser than number 2 ","Ans : ",num1<num2)
        break
    elif operator==">":
        print("Number 1 is Greater than Number 2","Ans : ",num1>num2 )
        break
    elif operator=="=":
        print("Both the number is equal")
        break   
    else:
        print("You enter the Invalid Operator Plz enter the Valid operator")
        break
    
        
    




        
