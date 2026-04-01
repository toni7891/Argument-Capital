import storage
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

    def find_account(acc_id):
        #store all data
        all_clients = storage.all_clients()

        #search for nedded acc 
        for client_id, info in all_clients.items():
            if client_id == acc_id:
                return client_id, info #* return tuple (id , info)
                # print(client_id)
                # print(info)
            else:
                return False


    def deposit(amount, client_id_input):
        #* stores all data from json *VERY IMPORTANT*
        all_clients = storage.all_clients()

        for client_id, client_info in all_clients.items():
            if client_id == client_id_input:
                if amount > 0:

                    client_info["balance"] += amount

                    new_transaction = {
                        "type": "deposit",
                        "from": all_clients[client_id]["username"],
                        "to": all_clients[client_id]["username"],
                        "amount": amount,
                        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "direction": "in"
                    }

                    #* add new transaction to list of all transactions
                    all_clients[client_id_input]["transaction_list"].append(new_transaction)

                    #* rewrite to json with new data 
                    storage.save_clients(all_clients_save=all_clients)

                    return True


    def transaction_fromto(amount,from,to):
        pass
    
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
    # Client.find_account("100")
    print(Client.deposit(amount=500, client_id_input="100")) #?--> אמור להכניס 500 לאיידי 100
    # storage.save_clients()
    #Client.from_dict(storage.all_clients())
    # x = 0
    

if __name__ == "__main__":
    main()



























