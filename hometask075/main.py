x=0
sp=[123,234,345,456]
for i in range(len(sp)):
    print(sp[i])
n=int(input('Введите число'))
for i in range(len(sp)):
    if sp[i]==n:
        print(i)
    else:
         x+=1
if x == 4:
    print('This is not in the list')