import math

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)



def errorr(ac,an):
    ea = abs((ac-an)/ac)*100
    return ea


ea=100
es=(0.5*10**-8)*100
signo=0
serie=1-(-0.85)
count=1

exponentes_i=2
while ea>=es:
    ac = serie
    print(ac)
    if signo==0:
        serie =serie+((-0.85**exponentes_i)/factorial(exponentes_i))
        paso = signo+1
    else:
        signo= signo-1
        serie =serie-((-0.85**exponentes_i/factorial(exponentes_i)))
    an = serie
    
    ea = errorr(ac,an)
    count = count+1
    exponentes_i = exponentes_i+1

    
print("Valor serie: ",serie)
print("Error relativo porcentual: ",ea)
print("# iteraciones ",count)