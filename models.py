import storage
import json
from datetime import *
from time import *
import random

class Client:
    def __init__(self, client_ID, username, pin, balance, blocked_or_not, is_admin, transaction_list):
        self.client_ID = client_ID
        self.username = username
        self.pin = pin
        self.balance = balance
        self.blocked_or_not = blocked_or_not
        self.is_admin = is_admin
        self.transaction_list = transaction_list
        
    # writing data to json file in correct format
    def to_dict(self):
         return {
            "client_ID": self.client_ID,
            "username": self.username,
            "pin": self.pin,
            "balance": self.balance,
            "blocked_or_not": self.blocked_or_not,
            "is_admin": self.is_admin,
            "transaction_list": self.transaction_list,
        }
        




    # def from_dict(data):
    
    #     # list to store all clients data as class object
    #     clients_objects = []    
    #     # print(data)
    #     # sort and map and add to list
    #     for client_ID, client_info in data.items():
    #         map_user = Client(client_ID=client_ID, **client_info) #*--> here the conversion from dict [json] to class type happens!
    #         clients_objects.append(map_user)
    #     return clients_objects #* returns all clients data (if we have time add encryption)


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
                    old_balance = all_clients[client_id]["balance"]
                    all_clients[client_id]["balance"] += amount
                    new_balance = all_clients[client_id]["balance"]
                    type_of_operation = "deposit"
                    direction = "in"

                    new_transaction = (storage.transaction_format(type_of_operation, all_clients[client_id]["username"], all_clients[client_id]["username"], amount, direction, old_balance, new_balance))

                    #* add new transaction to list of all transactions
                    all_clients[client_id_input]["transaction_list"].append(new_transaction)

                    #* rewrite to json with new data 
                    storage.save_clients(all_clients_save=all_clients)

                    return True
            
        error = "The amount You want to deposit is less or equal to zero!"
        return error


    def transaction_fromto(amount, from_id, to_id):
        """
            function to transfer funds from one account to another
            gets amount[int] (of funds)
                 from_id[str] (acc id of whos transfering)
                 to_id][str] (acc id who gets the funds)

            then changing and saving the transfer and the transaction hisrtory in the json file
        """

        #* store all clients
        all_clients_trans = storage.all_clients()
        type_of_operation = "transfer"

        #* find client who wants to transfer and their data
        for client_id1, client_info1 in all_clients_trans.items():
            if from_id == client_id1:
                #* save from acc data
                trans_from_id = client_id1          
                trans_from_info = client_info1
                old_balance_from = all_clients_trans[trans_from_id]["balance"]
                if all_clients_trans[trans_from_id]["balance"] < amount: 
                    return "insuffecient funds in account"
                
                #* find client who will get the payment
                for client_id2, client_info2 in all_clients_trans.items():
                    if to_id == client_id2:
                        
                        #data from who recive transfer
                        trans_to_id = client_id2       
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

                
                return "destenation account does not exist!"
                
                
        return "account from where to transfer does not exist!"
            
    
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
                    
    
    def change_pin(client_id, old_pin, new_pin):
        all_clients = storage.all_clients()
        
        
        for client_num, client_info in all_clients.items():
            if client_num == client_id and client_info["pin"] == old_pin:
                all_clients[client_id]["pin"] = new_pin
                storage.save_clients(all_clients)

                return True

        return "Error! one or more credentials is incorrect try again"
            

    
    def withdraw(amount, client_id_input):
        #* stores all data from json *VERY IMPORTANT*
        all_clients = storage.all_clients()
        print(all_clients)

        for client_id, client_info in all_clients.items():
            if client_id == client_id_input:
                old_balance = all_clients[client_id]["balance"]

                if float(amount) < old_balance:
                    all_clients[client_id]["balance"] -= amount
                    new_balance = all_clients[client_id]["balance"]
                    type_of_operation = "withdrawl"
                    direction = "out"

                    new_transaction = (storage.transaction_format(type_of_operation, all_clients[client_id]["username"], all_clients[client_id]["username"], amount, direction, old_balance, new_balance))

                    #* add new transaction to list of all transactions
                    all_clients[client_id_input]["transaction_list"].append(new_transaction)

                    #* rewrite to json with new data 
                    storage.save_clients(all_clients_save=all_clients)

                    return True
                
        return "Insuffiecnt funds!"
                


class Admin(Client):
    def __init__(self, client_ID, username, pin):
        super().__init__(client_ID=client_ID, username=username, pin=pin, balance=0.0, blocked_or_not=False, is_admin=True, transaction_list=[])
        
        
        # TODO --> need to make this function!
    # thats how the function is called -> Client.create_client_account(username="test", pin="1234", balance=999, blocked_or_not=False, is_admin=False)
    def create_client_account(username, pin, balance, blocked_or_not, is_admin):
        all_clients = storage.all_clients()
        is_unique = False
        # Check if client ID already exists
        while is_unique == False: 
            new_client_id = random.randint(103, 999)
            if new_client_id not in all_clients:
                is_unique = True
                
        trans_history = []

        new_client = Client(new_client_id, username, pin, balance, blocked_or_not, is_admin, trans_history)
        
        dict_client = Client.to_dict(new_client)
        
        all_clients[new_client.client_ID] = dict_client
        
        #write to json
        storage.save_clients(all_clients)
        
        
        
    def show_all_client_data():
        all_clients = storage.all_clients()
        all_clients_formatted = []
        for client_id , client_data in all_clients.items():
            if client_data["is_admin"] == False:
                all_clients_formatted.append({
                    "client_ID": client_id["client_ID"],
                    "username": client_data["username"],
                    "pin": client_data["pin"],
                    "balance": client_data["balance"],
                    "blocked_or_not": client_data["blocked_or_not"],
                    "is_admin": client_data["is_admin"],
                    "transaction_list": client_data["transaction_list"]
                    })
                
        return all_clients_formatted   
        
    
    def block_client(client_toblock):
        all_clients = storage.all_clients()
        
        for client_id, client_info in all_clients.items():
            if client_id == client_toblock:
                all_clients[client_id]["blocked_or_not"] = True
                return True
        return "error! client not found!"


def main():
    # Client.find_account("100")
    # # Client.deposit(amount=500, client_id_input="100") #?--> אמור להכניס 500 לאיידי 100
    # storage.save_clients()
    #Client.from_dict(storage.all_clients())
    # x = 0
    # Client.transaction_fromto(amount=500, from_id="100", to_id="102")
    #Client.check_pin(pin_input=1234, id_input=100)
    #Admin.create_client_account(username="test123", pin="1234", balance=999, blocked_or_not=False, is_admin=False)
    Client.change_pin("676", "1234", "4321")

    #Client.withdraw(amount=100, client_id_input="100")
    # Client.check_pin(pin_input=1234, id_input=100)
    # Client.change_pin("1234", "100", "5678")




if __name__ == "__main__":
    main()



























