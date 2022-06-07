# 1.	Найти НОК двух чисел
a = int(input('inter ferst number: '))
b = int(input('inter second number: '))
if a > b:  
        temp = b 
else: 
        temp = a 
for i in range(1, temp + 1): 
        if(( a % i == 0) and(b % i == 0 )): 
            devide = i
x = a // devide
y = b // devide
result = devide * x * y
print (result)