#---- functions and recursion---- in python ------

def add(a,b):
   sum=a+b  #1 add
   return sum
def sub(a,b):
   sub=a-b  #2 subtract
   return sub
def mul(a,b):
   mul=a*b  #3 multiply
   return mul
def div(a,b):
   div=a/b  #4 divide
   return div
def floor_div(a,b):
   floor_div=a//b #5 floor division
   return floor_div
def pow(a,b):
   pow=a**b     #6 power
   return pow
def mod(a,b):  
   mod=a%b #7 modulo
   return mod
print("----- Calculator -----")            
a=float(input("Enter first number : "))
b=float(input("Enter second number : "))
operator=input("Enter the operator (+,-,*,/,//,**,%) : ")
if operator=='+':
   print("Addition of number is : ",add(a,b))
elif operator=='-':
   print("Subtraction of numbers is :",sub(a,b))
elif operator=='*':
   print("Multiplication of number is :",mul(a,b))      
elif operator=='/':
   if b==0:
      print("Second number can't be Zero. ")
   else:
      print("Division of numbers :",div(a,b))
elif operator=='//':
   if b==0:
         print("Second number can't be Zero. ")
   else:
         print("Floor division of numbers :",floor_div(a,b))
elif operator=='%':
   if b==0:
         print("Second number can't be Zero. ")
   else:
         print("Modulo of numbers :",mod(a,b)) 
elif operator=='**':
    print("Solution of numbers : ",pow(a,b))
else:
    print("You have chosen invalid input. ")
print("End of the program")        
      
