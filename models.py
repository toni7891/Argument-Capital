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


    def deposit(amount, client_id_input):
        if amount < 0:
            return False
        
        #* stores all data from json *VERY IMPORTANT*
        all_clients = storage.all_clients()
        
        
        # finding client and info
        for client_id, client_info in all_clients.items():
            if client_id == client_id_input:
                
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


    def transaction_fromto(amount, from_id, to_id):
        """
            function to transfer funds from one account to another
            gets amount[int] (of funds)
                 from_id[str] (acc id of whos transfering)
                 to_id][str] (acc id who gets the funds)

            then changing and saving the transfer and the transaction hisrtory in the json file
        """
        all_clients_trans = storage.all_clients()
        to_id = to_id.replace(" ","")

        if all_clients_trans[from_id]["balance"] < amount: 
            return False

        #* store all clients
        type_of_operation = "transfer"

        #* find client who wants to transfer and their data
        for client_id1, client_info1 in all_clients_trans.items():
            if from_id == client_id1:
                #* save from acc data
                trans_from_id = client_id1          
                trans_from_info = client_info1
                old_balance_from = all_clients_trans[trans_from_id]["balance"]
                
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

                
                return False
                
                
        return False
            
    
    def check_pin(client_id, client_pin): #*--> checks the pin that was given to it for the id that was given to it.
        
        all_clients = storage.all_clients()
        client_id = client_id.replace(" ","")
        client_pin = client_pin.replace(" ","")
        
        for client_ID , client_info in all_clients.items():
            if client_ID == client_id and client_info["pin"] == client_pin:
                if client_info["blocked_or_not"] == True:
                    return 2
                return True
        return False   
                    
    
    def change_pin(client_id, old_pin, new_pin):
        all_clients = storage.all_clients()
        client_id = client_id.replace(" ","")
        old_pin = old_pin.replace(" ","")
        new_pin = new_pin.replace(" ","")
        
        
        for client_num, client_info in all_clients.items():
            if client_num == client_id and client_info["pin"] == old_pin:
                all_clients[client_id]["pin"] = new_pin
                storage.save_clients(all_clients)

                return True

        return False
            

    
    def withdraw(amount, client_id_input):
        #* stores all data from json *VERY IMPORTANT*
        all_clients = storage.all_clients()

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
                
        return False
                


class Admin(Client):
    def __init__(self, client_ID, username, pin):
        super().__init__(client_ID=client_ID, username=username, pin=pin, balance=0.0, blocked_or_not=False, is_admin=True, transaction_list=[])
        
        
        
    # thats how the function is called -> Admin.create_client_account(username="test", pin="1234", balance=999, blocked_or_not=False, is_admin=False)
    def create_client_account(username, pin, balance, blocked_or_not, is_admin):
        all_clients = storage.all_clients()
        pin1 = pin.replace(" ","")
        balance1 = float(balance)

        is_unique = False
        # Check if client ID already exists
        while is_unique == False: 
            new_client_id = random.randint(103, 999)
            if new_client_id not in all_clients:
                is_unique = True
                
        if balance1 < 0:
            return False

        trans_history = []
        
        new_client = Client(new_client_id, username, pin1, balance1, blocked_or_not, is_admin, trans_history)
        
        dict_client = Client.to_dict(new_client)
        
        all_clients[new_client.client_ID] = dict_client
        
        #write to json
        storage.save_clients(all_clients)
        
        
        
    def show_all_client_data():
        all_clients = storage.all_clients()
        all_clients_formatted = []
        for client_id , client_data in all_clients.items():
            if client_data["is_admin"] == False:
                all_clients_formatted.append(client_data)
                
        return all_clients_formatted   
        
    
    def block_client(client_toblock, BlockVar):
        all_clients = storage.all_clients()
        
        for client_id, client_info in all_clients.items():
            if BlockVar == True:
                if client_id == client_toblock:
                    all_clients[client_id]["blocked_or_not"] = True
                    storage.save_clients(all_clients)
                    return True
                elif BlockVar == False:
                    all_clients[client_id]["blocked_or_not"] = False
                    storage.save_clients(all_clients)
                    return True
        return False

    
    def add_to_admin(client_toadmin):
        all_clients = storage.all_clients()
        
        for client_id , client_info in all_clients.items():
            if client_id == client_toadmin:
                all_clients[client_id]["is_admin"] = True
                storage.save_clients(all_clients)
                return True
        return False

    def check_admin_login(admin_id, admin_pin): #*--> checks the pin that was given to it for the id that was given to it.
        
        all_clients = storage.all_clients()
        
        for client_id , client_info in all_clients.items():
            if client_info["is_admin"] == True:
                if client_id == admin_id and client_info["pin"] == admin_pin:
                    if client_info["blocked_or_not"] == True:
                        return False
                    return True
        return False   
    
    def find_account(acc_id):
        #store all data
        all_clients = storage.all_clients()

        #search for nedded acc 
        for client_id, info in all_clients.items():
            if client_id == acc_id:
                return info #* return tuple (id , info)
        return False
    
    def delete_account(client_id):
        all_clients = storage.all_clients() # Load your JSON

        for client_ID , client_info in all_clients.items():
            if client_ID == client_id:
                del all_clients[client_id] # Remove the key
                # Save the updated dictionary back to the JSON file
                storage.save_clients(all_clients)
                return True
        return False

def main():
    # Client.find_account("100")
    # # Client.deposit(amount=500, client_id_input="100") #?--> אמור להכניס 500 לאיידי 100
    # storage.save_clients()
    #Client.from_dict(storage.all_clients())
    x = 0
    # Client.transaction_fromto(amount=500, from_id="100", to_id="102")
    #Client.check_pin(pin_input=1234, id_input=100)
    #Admin.create_client_account(username="test123", pin="1234", balance=999, blocked_or_not=False, is_admin=False)
    #Client.change_pin("676", "1234", "4321")
    #Admin.block_client("508")
    #Client.withdraw(amount=100, client_id_input="100")
    # Client.check_pin(pin_input=1234, id_input=100)
    # Client.change_pin("1234", "100", "5678")
    # Admin.add_to_admin("508")
    # print(Admin.show_all_client_data())
    #print(Admin.check_admin_login("508","1234"))
    #Admin.create_client_account(username="test_fixes3", pin="1 23 4", balance="0  ", blocked_or_not="true   ", is_admin="false   ")
    #print(Admin.delete_account("531"))

if __name__ == "__main__":
    main()