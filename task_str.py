# Задача 1
volume_disket = 1.44 * 1024 * 1024
page = 100
line = 50
symbol = 25
inf_symbol = 4
volume_book = page * line * symbol * inf_symbol
nun_book = volume_disket // volume_book

print (nun_book)

#Задача 2
s = 5
r = 5
pi = 3.1415
area_c = pi * r ** 2
length = 2 * pi * r
perimeter = 4 * s
area_s = s ** 2
print(round(area_c, 2))
print(area_s, )
print(round(length,2))
print(perimeter)

#Задача 3
a = '0'
b = '1'
c = '2'
str_number =  (a * 20) + (b * 50) + (c * 30)
print(str_number)

#Задача 4
speed = 4096
time = 120
coast = 0.125
free = 500
speed_in_kd_in_sec = speed / 1024
time_in_sec = time * 60
file = speed_in_kd_in_sec * time_in_sec
money = (file-free) * coast
print(file)
print(money)

#Задача 5
length = 90
width= 50
perimeter = (length + width) * 2
print(perimeter)




