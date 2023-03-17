A = set()
B= {2, 5, 7, 9, 15, 22, 33}
C=set()

num=3



for i in range(7,31):
  A.add(i)

while num>=3 and num<30:
  if num%3==1:
    C.add(num)
    num=num+1
  else:
      num+=1
  


print(A)
print(B)
print(C)

def union (lista_1,lista_2):
    coso=lista_1.union(lista_2)
    return coso

def interseccion(lista_1,lista_2):
  coso=lista_1.intersection(lista_2)
  return coso

def diferencia(lista_1,lista_2):
  dif=lista_1.difference(lista_2)
  return dif

def simetrica(lista_1,lista_2):
  coso=lista_1.symmetric_difference(lista_2)
  return coso
    



print("------")

print("\n",union(interseccion(A,C),simetrica(A,B)))

print("\n",interseccion(simetrica(B,union(A,C)),diferencia(A,C)))


print("\n",interseccion(diferencia(union(A,B),interseccion(A,C)),union(union(A,B),union(B,C))))













    
      

    
  
