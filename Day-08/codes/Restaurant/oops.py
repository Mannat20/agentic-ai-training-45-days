'''
Create a food delivery app, where customer accesses a menu and places an order
the order can be vissualized on some admin panel or through email
and inhouse delivery person will deliver the order

    Identify the Objects
    Visualize the Objects
    Relate the Objects
    Code the Objects (Textually Define)
    Create the real objects in memory

1: Object: Restaurant
Attributes: name, phone, email, address, operating_hours, rating, price_per_person,menu

1: Menu
name, type, dishes[]

*: Dish
name, price, category, rating

Relationship Mapping for Objects
    1 to 1, 1 to *, * to *

    1 Restaurant has 1 Menu
    1 Menu has many Dishes

------------------------------------------    '''

#  2. Textually Represent the Object
# coding the object by writing the class

class Restaurant:
    pass

class Menu:
    pass

class Dish:
    pass    

#------------------------------------------ 

# Create Object in Memory
# Object Construction Statemen
restaurant=Restaurant()
menu=Menu()
dish1=Dish()
dish2=Dish()
dish3=Dish()

print('restaurant:', restaurant)
print('menu:', menu)

print('dish1:', dish1)
print('dish2:', dish2)
print('dish3:', dish3)

print('data in restaurant:', vars(restaurant))
print('data in menu:', vars(menu))
print('data in dish1:', vars(dish1))
print('data in dish2:', vars(dish2))
print('data in dish3:', vars(dish3))