

x=[1,2,3,4,5,6,7]
y=[0.2 , 0.5 , 1.8 , 3.4 , 5.7 , 9 , 13.8]

n=(len(x))
sumaX=0
sumaY=0 
sumaXelevado=0
sumaXY=0

for elem in y: 
  sumaY+=elem

promedioY=sumaY/n 

for elem in x: 
  sumaX+=elem

  elevado=elem**2
  sumaXelevado+=elevado
promedioX=sumaX/n

for i in range(len(x)):
  sumaXY+=x[i]*y[i]

a1=(n*sumaXY-sumaX*sumaY)/(n*sumaXelevado-(sumaX)**2)

a0=promedioY-a1*promedioX 

print("El resultado de a1 es igual a:", a1, "El resultado de a0 es igual a:", a0)


sr=0 
st=0 

for elem in y:

  st+= (elem-promedioY)**2

for i in range (len(x)):
  sr+= (y[i]-a0-a1*x[i])**2

print(f"sr: {sr}")  
print(f"st: {st}")

r2= ((st-sr)/st)

r= (((r2)**0.5))*100

print(f"r2: {r2}")  
print(f"r: {r}")



  




