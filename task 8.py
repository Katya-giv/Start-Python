for i in range(3):
    print(i+1,"шаг цикла")
print("Первый цикл закончился!")

a = {1: 'x', 2: 'y', 3: 'z'}
for index, value in a.items():
    print(f'"Позиция": {index} -> "Значение": {value}')


for value in range(10):
    print(f' Значение: {value}')
# range(1,11)
# range(1,11,2)
# range(10,0,-1)

for  tuple_ in enumerate (["а","б","в"]) :
    print(tuple_)

for pos, value in enumerate ("абв", start=1) :
    print("Позиция:",pos,"->", "Значение:", value)

#Задача 1
 a,s,p = 1,150,200
 while True:
     if a>10:
         break
         a += 2
         p += a
         s += p




