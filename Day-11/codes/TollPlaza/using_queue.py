class TollPlazaQueue:
    def __init__(self):
        self.front=None
        self.end=None
        self.size=0
        print('[TollPlazaQueue] [init] Queue Constrcuted', self)

    def add(self,vehicle):
        self.size +=1
        if self.front==None:
            self.front=vehicle
            self.end=vehicle
        else:
            self.end.next=vehicle
            self.front.previous= vehicle
            vehicle.previous=self.end
            vehicle.next=self.front
            self.end=vehicle
    
    def deduct_toll_tax(self,vehicle):
        print(f'FastTag balance for {vehicle.registration_number} having balance | \u20b9 {vehicle.fastTag.Balance}')
        if vehicle.type=='4w':
            if vehicle.fastTag.Balance > 100 :
                vehicle.fastTag.Balance -= 100
                print('\n Toll Deducted')
                print(f' New FastTag blance for {vehicle.registration_number} having balance | \u20b9 {vehicle.fastTag.Balance}')
                self.delete()
            else :
                print(f'{vehicle} has low balance')

        else:
            if vehicle.fastTag.Balance>50:
                vehicle.fastTag.Balance -=50
                print('\n Toll Deducted')
                print(f' New FastTag blance for {vehicle.registration_number} having balance | \u20b9 {vehicle.fastTag.Balance}')
                self.delete()
            else:
                print(f'{vehicle} has low balance')
        
    def delete(self):
        self.front=self.front.next
        self.size -=1

    def show(self,traverse=True):
        if traverse==True:
            flight=self.front
            while True:
                flight.show()
                flight=flight.next
                if flight==self.front:
                    break
        else:
            flight=self.end
            while True:
                flight.show()
                flight=flight.previous
                if flight==self.end:
                    break