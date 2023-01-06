import math 

def substraction(x,y):
 sum = x-y
 return sum

def askinlength():
  userInput1 = float(input("Enter the first number"))
  userInput2 = float(input("Enter the second number"))
  userInput3 = float(input("Enter the third number(1st)"))
  userInput4 = float(input("Enter the fourth number(2nd)"))
  result1 = substraction(userInput1, userInput2)
  Absresult1 = abs(result1)
  result2 = substraction(userInput3, userInput4)
  Absresult2 = abs(result2)
  TotalSize = Absresult1*Absresult2
  return TotalSize
TotalSize = askinlength()

def layout():
  print(str(TotalSize))
  
layout()
  
     
  
  
