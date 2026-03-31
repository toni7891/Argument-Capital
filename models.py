from storage import *
import json

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
    # @staticmethod

    def from_dict(data):

        clients_objects = []    
        for client_ID, client_info in data.items():
            map_user = Client(client_ID=client_ID, **client_info) #*--> here the conversion from dict to class happens!
            clients_objects.append(map_user)
        return clients_objects
    
    
# TestClient = Client("100", "guy_peres", "1234", "2000", "False", "[]")    
    

    def find_account(which_acc, filename="data.json"):
            #read the data.json and store client data in data var 
            with open(filename, "r") as file:
                data = json.load(file)

            #making list full of clients (as class object)
            all_clients = Client.from_dict(data)
            
            counter = (len(all_clients) - 1)

            #cycling thourgh every client to find the nedded one
            for client in all_clients:
                # cycling until last client in the list
                if counter > -1:

                    #checking each client
                    if all_clients[counter]:

                        #if needed clientID exist then good
                        if client.client_ID == which_acc:
                            return True

                        #if not then error
                        elif counter == 0:
                            return False

                    #cycle counter iteration
                    counter -= 1

            
    
    def check_pin(client, pin_input):
        if(client.pin == pin_input):
            return True
        else:
            return None
            #! WARNING MESSAGE NEEDED HERE
            
    def deposit(client):
        pass
    
    def withdraw():
        pass
    
Client.find_account("100")




























