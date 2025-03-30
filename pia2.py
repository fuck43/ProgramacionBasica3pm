def funcion(n):
    m=str(n)
    chars=list(m) 
    sum=0
    for e in chars: 
        sum+=int(e)
    return sum 

while True:
    n = input("ingresa un numero: ")
    print(funcion(n)) 





