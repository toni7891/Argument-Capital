import test_storage
import json
from datetime import *
from time import *


class Client:
    def __init__(self, client_ID, username, pin, balance, blocked_or_not, transaction_list):
        self.client_ID = client_ID
        self.username = username
        self.pin = pin
        self.balance = balance
        self.blocked_or_not = blocked_or_not
        self.transaction_list = transaction_list
        
        
    # writing data to json file
    def to_dict(self):
        return {
            "client_ID": self.client_ID,
            "username": self.username,
            "pin": self.pin,
            "balance": self.balance,
            "blocked_or_not": self.blocked_or_not,
            "transaction_list": self.transaction_list
        }
        
    # used to define function under a class but not needing to use the class ex -> 
    # from:  Client().func()
    # to: Client.func()
    # [not in use now]
    @staticmethod

    def from_dict(data):

        # list to store all clients data as class object
        clients_objects = []    
        # print(data)
        # sort and map and add to list
        for client_ID, client_info in data.items():
            map_user = Client(client_ID=client_ID, **client_info) #*--> here the conversion from dict [json] to class type happens!
            clients_objects.append(map_user)
        return clients_objects #* returns all clients data (if we have time add encryption)

    def find_account(which_acc):

            get_clients = None
            get_clients = storage.all_clients()
            
            counter = (len(get_clients) - 1)

            #cycling thourgh every client to find the nedded one
            for client in get_clients:
                # cycling until last client in the list
                if counter > -1:

                    #checking each client
                    if get_clients[counter]:

                        #if needed clientID exist then good
                        if client.client_ID == which_acc:
                            print(client.client_ID)
                            return True

                        #if not then error
                        elif counter == 0:
                            return False

                    #cycle counter iteration
                    counter -= 1
                    

    def new_find_account(acc_id):
        all_clients = test_storage.all_clients()
        for client_id, info in all_clients.items():
            if client_id == acc_id:
                print(client_id)
                print(info)


 #! NEEDS FIXING! 
    def deposit(amount, client_id_input, filename="data.json"):
                    #read the data.json and store client data in data var 
        get_clients = None
        get_clients = storage.all_clients()
        client_list_to_giveback = []
        counter = (len(get_clients) - 1)
            #cycling thourgh every client to find the nedded one
        for client in get_clients:
                # cycling until last client in the list
                if counter > -1:

                    #checking each client
                    if get_clients[counter]:
                        
                        if amount > 0:
                            #if the amount is bigger then zero
                            
                        #if account is found and the if is true, work on the client that is found
                            if Client.find_account(client_id_input): #! problem might be here
                                client.balance += amount
                                # print("money should've been deposited")
                                
                                # return (f"the amount of {amount} has been deposited to your account")
                                
                             #if not then error
                            elif counter == 0:
                                pass             
                    client_list_to_giveback.append(client) #! problem might be here
                
                counter -= 1
        storage.save_clients(client_list_to_giveback) #! problem might be here
            
    
    def check_pin(client, pin_input):
        if(client.pin == pin_input):
            return True
        else:
            return None
            #! WARNING MESSAGE NEEDED HERE
            
    def deposit_old(client):
        pass
    
    def withdraw():
        pass
    
def main():
    Client.new_find_account("100")
    # Client.deposit(500, 100) #?--> אמור להכניס 500 לאיידי 100
    # storage.save_clients()
    #Client.from_dict(storage.all_clients())
    x = 0
    

if __name__ == "__main__":
    main()



























