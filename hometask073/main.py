sp={}
for i in range(1,5):
    b=input('Введите любимое блюдо:')
    sp.update({i:b})
print(sp)
#bf=input('Введите блюдо которое хотите удалить')
bn=int(input('Введите номер блюда которое хотите удалить'))
sp.pop(bn)



print(sp)