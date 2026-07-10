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

flight_list.add_in_front(flight1)

# print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# print('After adding 1st flight')
# print(vars(flight_list))
# print(vars(flight1))
# print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~')

flight2=flight(
    name='Air India',
    number='AI 7713',
    departure_time='11:05',
    departure_loc='LDH',
    duration='08h 45m',
    message='Non Stop',
    arrival_time='08:20',
    arrival_loc= 'ZRH',
)
flight_list.add_in_front(flight2)
# print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# print('After adding 2nd flight')
# print(vars(flight_list))
# print(vars(flight1))
# print(vars(flight2))
# print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~')
flight3=flight(
    name='Indigo',
    number='IN 7790',
    departure_time='11:05',
    departure_loc='DEL',
    duration='08h 45m',
    message='Non Stop',
    arrival_time='08:20',
    arrival_loc= 'LEh',
)

flight4=flight(
    name='Indigo',
    number='IN 7767',
    departure_time='08:05',
    departure_loc='DEL',
    duration='05h 45m',
    message='Non Stop',
    arrival_time='02:20',
    arrival_loc= 'Kashmir',
)
flight5=flight(
    name='Air India',
    number='AI 7882',
    departure_time='11:05',
    departure_loc='DEL',
    duration='08h 45m',
    message='Non Stop',
    arrival_time='08:20',
    arrival_loc= 'Mumbai',
)

flight_list.add_in_front(flight3)
flight_list.add_in_front(flight4)
flight_list.add_in_front(flight5)

print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('After adding 5th flight')
print(vars(flight_list))
print(vars(flight1))
print(vars(flight2))
print(vars(flight3))
print(vars(flight4))
print(vars(flight5))
print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~')