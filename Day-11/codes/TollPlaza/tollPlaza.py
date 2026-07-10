from Vehicle_FastTag import vehicle,fastTag
from using_queue import TollPlazaQueue

def main():
    
    """
    fasttag1 = FastTag(
            fasttag_id=4019, 
            bank='SBI', 
            balance=500)

    vehicle1 = Vehcile(
        registration_number='PB10AL2937', 
        type='4W', 
        fasttag=fasttag1
        )
    """

    vehicle1 = vehicle(
        registration_number='PB10AL2937', 
        type='4W', 
        fastTag=fastTag(
            fastTag_id=4019, 
            Bank='SBI', 
            Balance=500)
        )
    
    vehicle2 = vehicle(
        registration_number='KA12KC1212', 
        type='4W', 
        fastTag=fastTag(
            fastTag_id=7890, 
            Bank='ICICI', 
            Balance=600)
        )
    
    vehicle3 = vehicle(
        registration_number='HR20AB1122', 
        type='4W', 
        fastTag=fastTag(
            fastTag_id=6609, 
            Bank='ICICI', 
            Balance=50)
        )
    
    vehicle4 = vehicle(
        registration_number='PB10KC1220', 
        type='4W', 
        fastTag=fastTag(
            fastTag_id=5152, 
            Bank='SBI', 
            Balance=1000)
        )
    
    vehicle5 = vehicle(
        registration_number='PB10BD3027', 
        type='2W', 
        fastTag=fastTag(
            fastTag_id=2234, 
            Bank='SBI', 
            Balance=20)
        )



    queue = TollPlazaQueue()
    queue.add(vehicle1)
    queue.add(vehicle2)
    queue.add(vehicle3)
    queue.add(vehicle4)
    queue.add(vehicle5)

    queue.show()

    # After adding Vehcile in Queue, deduct the toll
    queue.deduct_toll_tax(vehicle1)
    queue.deduct_toll_tax(vehicle2)
    queue.deduct_toll_tax(vehicle3)
    queue.deduct_toll_tax(vehicle4)
    queue.deduct_toll_tax(vehicle5)

    print(f'Size of Queue is: {queue.size}')

if __name__ == '__main__':
    main()