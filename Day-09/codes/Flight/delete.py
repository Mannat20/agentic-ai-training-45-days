from flight import flight
from circular_doubly_linked_list import list

flight_list=list()
print(vars(flight_list))

flight1=flight(
    name='Air India',
    number='AI 7713',
    departure_time='01:05',
    departure_loc='DEL',
    duration='08h 45m',
    message='Non Stop',
    arrival_time='06:20',
    arrival_loc= 'ZRH',
)
flight_list.add(flight1)
# flight2=flight(
#     name='Air India',
#     number='AI 7713',
#     departure_time='11:05',
#     departure_loc='LDH',
#     duration='08h 45m',
#     message='Non Stop',
#     arrival_time='08:20',
#     arrival_loc= 'ZRH',
# )
# flight3=flight(
#     name='Indigo',
#     number='IN 7790',
#     departure_time='11:05',
#     departure_loc='DEL',
#     duration='08h 45m',
#     message='Non Stop',
#     arrival_time='08:20',
#     arrival_loc= 'LEh',
# )



# flight_list.add(flight2)
# flight_list.add(flight3)

# print('\n------------------------')
# print(vars(flight_list))
# print(vars(flight1))
# print(vars(flight3))
# print(vars(flight2))
# print('------------------------')

print(vars(flight_list))
# flight_list.delete_last()
# flight_list.delete_front()
flight_list.delete(flight1)
print('\nafter deletion:\n')

print(vars(flight_list))
# flight_list.show(traverse=True)