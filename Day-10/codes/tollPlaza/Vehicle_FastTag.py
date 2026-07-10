# Vehicle: registration_number, type, fasttag
# FastTag: fasttag_id, bank, balance

# 1 Vehicle has 1 FastTag

class fastTag:
    def __init__(self,fastTag_id,Bank,Balance):
        self.fastTag_id=fastTag_id
        self.Bank=Bank
        self.Balance=Balance
        print(f'[fastTag] [LOG] {fastTag_id} constructed ')
    def show(self):
        print('~'*5 +'Fast Tag'+ '~'*5)
        print(f'{self.fastTag_id} | {self.Bank} | {self.Balance}')
        print('~'*10)
        

class vehicle:
    def __init__(self,registration_number,type,fastTag):
        self.registration_number=registration_number
        self.type=type
        self.fastTag=fastTag
        print(f'[vehicle] [LOG] queue constructed ')

    def show(self):
        print('~'*5 +'Fast Tag'+ '~'*5)
        print(f'{self.registration_number} | {self.type} ')
        self.fastTag.show()
        print('~'*10) 
