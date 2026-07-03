def sort(numbers,length):
    for i in range(length):
        for j in range(length-1-i):
            print('[LOG] i: ',i,' j; ',j)
            print('-----------')
            if(numbers[j]>numbers[j+1]):
                print('[LOG] Swapping ',numbers[j],' and ',numbers[j+1] ,' at Loop: ',i,' index:',j,' and ',j+1)
                print('-----------')
                numbers[j],numbers[j+1]=numbers[j+1],numbers[j]


data=[20,30,50,10,40]
result=sort(data,len(data))
print('Sorted list is ',data)
