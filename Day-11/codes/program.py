object={
    'vehicle':0,
    'fastTag':0,
    'TollPlazaQueue':0
}

file=open('tollPlaza.py','r')
lines= file.readlines()
for line in lines:
    for i in object:
        if i in line:
            object[i]+=1

with open('objectanalysis.csv','a') as files:
    for i in object:
        data=f'{i},{object[i]}\n'
        files.write(data)