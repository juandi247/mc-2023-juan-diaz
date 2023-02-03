a=int(input("escriba cuantos numeros para el conjunto A: "))

lista_1=set()
lista_2=set()

for i in range(a):
  numero=float(input("Num conjunto A: "))
  lista_1.add(numero)
print("----------")

b=int(input("escriba cuantos numeros para el conjunto b: "))
for m in range(b):
  segundo=float(input("Num conjunto B: "))
  lista_2.add(segundo)


print("\n")


while True:
  print(" 1.Union \n 2.interseccion \n 3.diferencia \n 4.diferencia simetrica  \n 5.salir \n")
  coso=int(input("\n"))
  if coso==1:
    union=lista_1.union(lista_2)
    print(union)
  if coso==2:
    intersec=lista_1.intersection(lista_2)
    print(intersec)
  if coso==3:
    dif=lista_1.difference(lista_2)
    dif_2=lista_2.difference(lista_1)
    print("A-b:",dif)
    print(f"B-A:{dif_2}")

  if coso==4:
    sim=lista_1.symmetric_difference(lista_2)
    print(sim)
  if coso==5:
    break
    
    
  


    
    
