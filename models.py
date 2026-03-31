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
        
        

    def to_dict(self):
        return {
            "client_ID": self.client_ID,
            "username": self.username,
            "pin": self.pin,
            "balance": self.balance,
            "blocked_or_not": self.blocked_or_not,
            "transaction_list": self.transaction_list
        }
        
        
    @staticmethod
    def from_dict(data):
        return Client(
            data["client_ID"],
            data["username"],
            data["pin"],
            data["balance"],
            data["blocked_or_not"],
            data["transaction_list"]
        )
    
    
# TestClient = Client("100", "guy_peres", "1234", "2000", "False", "[]")    
    


    
    # def check_pin(client, pin_input):
    #     if(client.pin == pin_input):
    #         return True
    #     else:
    #         return None
    #         #! WARNING MESSAGE NEEDED HERE
            
    # def deposit(client):
    #     pass
    
    # def withdraw():
    #     pass
 
def find_account(filename="data.json"):
    #read the data.json and store client data in data var 
    with open(filename, "r") as file:
        data = json.load(file)
        print(data)
