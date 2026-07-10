# import json
# order = {
#     'oid': 1, 
#     'customer': 'John',
#     'dishes': 'dal, paneer, roti',
#     'amount': 500
# }

# print(type(order))
# print(order)
# json_orders=json.dumps(order)
# print(type(json_orders))
# print(json_orders)
# loads
# Pythons Built In Module (JSON)
import json

order = {
    'oid': 1, 
    'customer': 'John',
    'dishes': 'dal, paneer, roti',
    'amount': 500
}

# print(type(order))
# print(order)

# Dictiory to JSON (String representation of Dictionary)
json_order = json.dumps(order)

print(type(json_order))
print(json_order)

# JSON to Dictiory (String converted to Dictionary)
order_dictionary = json.loads(json_order)
print(type(order_dictionary))
print(order_dictionary)