
#Юзер вводит значения переменных
x, y   = int(input("Enter x ")), int(input("Enter y "))

z = int(input("Enter z "))

#Сперва проверяем на четность, затем сравниваем между собой
#Если все нечетные
if x % 2 != 0 and y % 2 != 0 and z % 2 != 0:
    if  x > y and x > z:
        print ('x is largest odd number')
    elif y > z:
        print ('y is largest odd number')
    else:
        print ('z is largest odd number')
#Если x и y нечетные
elif x % 2 != 0 and y % 2 != 0:
    if x > y:
        print ('x is largest odd number')
    else:
        print ('y is largest odd number')
#Если y и z нечетные
elif y % 2 != 0 and z % 2 != 0:
    if y > z:
        print ('y is largest odd number')
    else:
        print ('z is largest odd number')
#Если x и z нечетные
elif x % 2 != 0 and z % 2 != 0:
    if x > z:
        print ('x is largest odd number')
    elif z % 2 != 0:
        print ('z is largest odd number')
# Если хотя бы одно число нечетное
elif x % 2 != 0 or y % 2 != 0 or z % 2 != 0: 
    if   x % 2 != 0:
        print ('x is largest odd number')
    elif y % 2 != 0:
        print ('y is largest odd number')
    elif z % 2 != 0:
        print ('z is largest odd number')
#Если все четные
else:
    print ('None of them are odd')