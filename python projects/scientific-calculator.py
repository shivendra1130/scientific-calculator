import math
print("//// WELCOME IN PYTHON SCIENTIFIC CALCULATOR ////")
print("Available operators: +, -, *, /, %, **, sqrt, fact, sin, cos, tan, q")
print("-------------------------------------------------")

while True:
 operator=input("\nchoose operator : ")
 
 if operator =="q":
  print("exiting calculator....")
  break

 if operator in ["sqrt", "fact", "sin", "cos", "tan"]:
  num=float(input("enter the number : "))

  if operator =="sqrt":
   print("sqaure root of number : ",math.sqrt(num))
 
  elif operator =="fact":
   print("factorial of num : ",math.factorial(int(num)))
 
  elif operator =="sin":
   print("sin value of num : " ,math.sin(math.radians(num)))
  
  elif operator =="cos":
   print("cos value of num : " ,math.cos(math.radians(num)))
  
  
  elif operator =="tan":
   print("tan value of num : " ,math.tan(math.radians(num)))

 else:
  
  num1=float(input("enter the value of 1st number : "))
  num2=float(input("enter the value of 2nd number : "))

  if operator=="+":
        print("addition of 1st and 2nd number : ",num1+num2 )
 
  elif operator=="-":
         print("substraction of 1st and 2nd number : ",num1-num2 )
  
  elif operator=="*":
         print("multiplication of 1st and 2nd number : ",num1*num2 )
  
  elif operator=="%":
         print("remender of 1st and 2nd number : ",num1%num2 )

  elif operator=="**":
         print("power of 1st and 2nd number : ",num1**num2 )


  elif operator=="/":
        if num2==0:
         print("denominator should not be zero")
        else:
         print("division of 1st and 2nd number : ",num1/num2 )

  else:  
   print("invalid operation!!!") 