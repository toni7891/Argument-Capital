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
    # def to_dict(self):
    #     return {
    #         "client_ID": self.client_ID,
    #         "username": self.username,
    #         "pin": self.pin,
    #         "balance": self.balance,
    #         "blocked_or_not": self.blocked_or_not,
    #         "transaction_list": self.transaction_list
    #     }
        
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
                    old_balance = client_info["balance"]
                    client_info["balance"] += amount
                    new_balance = client_info["balance"]
                    type_of_operation = "deposit"
                    direction = "in"

                    new_transaction = (storage.transaction_format(type_of_operation, all_clients[client_id]["username"], all_clients[client_id]["username"], amount, direction, old_balance, new_balance))

                    #* add new transaction to list of all transactions
                    all_clients[client_id_input]["transaction_list"].append(new_transaction)

                    #* rewrite to json with new data 
                    storage.save_clients(all_clients_save=all_clients)

                    return True


    def transaction_fromto(amount, from_id, to_id):
        """
            function to transfer funds from one account to another
            gets amount[int] (of funds)
                 from_id[str] (acc id of whos transfering)
                 to_id][str] (acc id who gets the funds)

            then changing and saving the transfer and the transaction hisrtory in the json file
        """


        all_clients_trans = storage.all_clients()
        type_of_operation = "transfer"

        for client_id1, client_info1 in all_clients_trans.items():
            if from_id == client_id1:
                #* save from acc data
                trans_from_id = client_id1          
                trans_from_info = client_info1
                old_balance_from = all_clients_trans[trans_from_id]["balance"]

                for client_id2, client_info2 in all_clients_trans.items():
                    if to_id == client_id2:
                        
                        trans_to_id = client_id2       #data from who recive transfer
                        trans_to_info = client_info2
                        old_balance_to = all_clients_trans[trans_to_id]["balance"]
    
                        #* changing balance and saving before after balance
                        all_clients_trans[trans_from_id]["balance"] -= amount
                        all_clients_trans[trans_to_id]["balance"] += amount

                        new_balance_from = all_clients_trans[trans_from_id]["balance"]
                        new_balance_to = all_clients_trans[trans_to_id]["balance"]


                        #* add transaction history
                        new_from_transaction = storage.transaction_format(type_of_operation, all_clients_trans[trans_from_id]["username"], all_clients_trans[trans_to_id]["username"], -amount, "out", old_balance_from, new_balance_from)
                        new_to_transaction = storage.transaction_format(type_of_operation, all_clients_trans[trans_from_id]["username"], all_clients_trans[trans_to_id]["username"], amount, "in", old_balance_to, new_balance_to)

            
                        #* add new transaction to list of all transactions
                        all_clients_trans[trans_from_id]["transaction_list"].append(new_from_transaction)
                        all_clients_trans[trans_to_id]["transaction_list"].append(new_to_transaction)

                        #* rewrite to json with new data 
                        storage.save_clients(all_clients_save=all_clients_trans)
                        return True

            
            
    
    def check_pin(pin_input, id_input): #*--> checks the pin that was given to it for the id that was given to it.
        
        all_clients_pin = storage.all_clients()
        for client_id1, client_info1 in all_clients_pin.items():
            if str(id_input) == client_id1:
                if all_clients_pin[client_id1]["pin"] == str(pin_input):
                    # print(f"the pin matchs! and its {all_clients_pin[client_id1]["pin"]}, for user - {all_clients_pin[client_id1]["username"]}")
                    return True
                else:
                    return False
        # print("pin doesnt match the user!")
                    
        
        



    
    # def withdraw():
        # pass
    
def main():
    # Client.find_account("100")
    Client.deposit(amount=500, client_id_input="100") #?--> אמור להכניס 500 לאיידי 100
    # storage.save_clients()
    #Client.from_dict(storage.all_clients())
    # x = 0
    # Client.transaction_fromto(amount=500, from_id="100", to_id="102")
    Client.check_pin(pin_input=1234, id_input=100)

if __name__ == "__main__":
    main()



























