class Bank:
    pass

class employee:
    def __init__(self,name,id,address,phone_number,email,salary):
        self.name=name
        self.id=id
        self.address=address
        self.phone_number=phone_number
        self.email=email
        self.salary=salary


class branch:
    def __init__(self,name,address,employees,id,phone_number,timings):
        self.name=name
        self.address=address
        self.employees=employees
        self.id=id
        self.phone_number=phone_number
        self.timings=timings

    


bank=Bank()
branch1=branch()
employee1=employee(
    'Rahul',101,'#34,ABC',7628635429,'rahul@gmail.com',67000
)
employee2=employee(
    'Anjali',102,'#78,ABC',9111176543,'Anjali@gmail.com',89000
)
employee3=employee(
    'Sam',103,'#90,SectarA',8999945555,'sam@gmail.com',90000
)
print('Bank: ',bank,vars(bank))
print('Branch: ',branch1,vars(branch1))
print('Employee1: ',employee1,vars(employee1))
print('Employee2: ',employee2,vars(employee2))
print('Employee3: ',employee3,vars(employee3))