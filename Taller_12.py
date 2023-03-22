from math import e
x=0.45
def factorial(num): 
    if num < 0: 
        print("Factorial of negative num does not exist")

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

fx=e**-x
fXX=-e**-x
contador=1
resultado=fx


h=0.005
elevado=1

print("iteracion ",(contador),": Resultado : ",resultado)
    
while contador<=16:
  
  if contador%2!=0:
    resultado=resultado+(fXX*h**elevado)/factorial(elevado)
    
  else:
    resultado=resultado+(fx*h**elevado)/factorial(elevado)
   
  elevado+=1
  contador+=1
  print("iteracion ",(contador),": Resultado : ",resultado)
    