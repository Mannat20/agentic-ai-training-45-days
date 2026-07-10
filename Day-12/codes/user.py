import hashlib
class user:
    def __init__(self,name=None,phone=None,email=None,password=None):
        self.name=name,
        self.phone=phone,
        self.email=email,
        self.password=password
    
    def input_details(self):
        self.name=input('Enter Name: ')
        self.phone=input('Enter phone: ')
        self.email=input('Enter email: ')
        self.password=input('Enter password: ')
        self.password=self.encrypt(self.password) # change the strings

    def show(self):
        print('~'*30)
        print(f'{self.name} | {self.phone} | {self.email} | {self.password}')
        print('~'*30)
     
    def encrypt(self,data):
        encrypted_data=hashlib.sha256(data.encode()).hexdigest()
        #sha256 is use when we want to only encrypt the data and this data can't be converted to original form. [sha512]
        return encrypted_data    
    def to_csv(self):
        return f'{self.name},{self.phone},{self.email},{self.password}'
    
    def to_dictionary(self):
        return vars(self)