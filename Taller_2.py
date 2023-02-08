A = set()
B= set()
C={1,3,8,10,12,15,18,20}
D=set()
num=1



for i in range(6,20+1):
  A.add(i)
for i in range(1,25):
  if i%2==0:
    B.add(i)

while num<46:
  count=1
  x=0
  while count<=num:
    if num%count==0:
      x+=1
    count+=1
  if x==2:
    D.add(num)
  num+=1



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
    


print(interseccion(B,(simetrica(C,D))))


print(union(interseccion(A,C),B))

print(diferencia(union(B,D),C))

print(simetrica(diferencia(A,B),(interseccion(A,D))))




    
      

    
  
