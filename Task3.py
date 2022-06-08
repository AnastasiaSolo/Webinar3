#1	Найти НОК двух чисел
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

#2 вычислить число Пи c заданной точностью d
#Пример: при d = 0.001,  c= 3.141. 

pi = 3 + 4/(2*3*4) - 4 /(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + 4/(10*11*12) - 4/(12*13*14)
def toFixed(pi, digits=0):
    return f"{pi:.{digits}f}"
print(toFixed(pi, 3))

#3.Составить список простых множителей натурального числа N
number=int(input("Integer: "))
for i in range(1, number+1):
    if(number%i==0) and (i != number) :
        print(i)

#4 Дана последовательность чисел. Получить список неповторяющихся элементов 
# исходной последовательности
#Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

numbers = [20, 20, 30, 30, 40, 50, 60, 70, 70]

def unique_numbers(numbers):
    unique = []

    for number in numbers:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique

print(unique_numbers(numbers))       