#3-cacular el factorial de numero dado
print("ingrese el numero")
num=int(input())
fact=1
for i in range(1, num+1):
    fact*=i
print("el factorial",num,"es:",fact)
#ulilize ciclo for y range para saber el facotrial