# Linear Search O(n)
'''def search(numbers,number_to_search):
    for item in numbers:
        if item==number_to_search:
            print('Found ',number_to_search,' in the list')
            break
    else:
        print('Not Found ',number_to_search,' in the list')
    

data=[10,20,30,40,50]
number_to_search=int(input('Enter number to search: '))
search(data,number_to_search)
'''

def search(*numbers,**number_to_search):
    for item in numbers:
        if item==number_to_search['key']:
            print('Found ',number_to_search['key'],' in the list')
            break
    else:
        print('Not Found ',number_to_search['key'],' in the list')
    
search(10,20,30,40,50,key=30)