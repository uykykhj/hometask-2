sp=[]

for i in range(3):
    n=input('ведите имя')
    sp.append(n)
x = input('Хотите добавить новые имена?')
if x=='yes':
    while x!='no' :

        n1=input('Введите имя')
        sp.append(n1)
        x = input('Хотите добавить новые имена?')
print(sp)
