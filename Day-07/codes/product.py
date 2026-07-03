def product(numbers,length):
    if length==0:
        return 1
    previous=product(numbers,length-1)
    current=numbers[length-1]
    return previous*current

data=[20,30,50]
result=product(data,len(data))
print('Product of ',data,' is ',result)