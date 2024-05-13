#Erick Javier Leiva León
#1146624

contador=1
sumatoria=0
while contador<=10:
    sumatoria+=(1/contador)
    print(contador)
    contador+=1
print(round(sumatoria,2))
print()

contador=0
sumatoria=1
while contador<=10:
    sumatoria+=(1/2**contador)
    print(contador)
    contador+=1
    print(round(sumatoria,2))
