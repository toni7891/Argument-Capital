import json
import models
from datetime import *
import os

MAIN_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(MAIN_DIR, "data.json")

def all_clients(filename=DATA_FILE):
    
    #read the data.json and store client data in data var 
    with open(filename, "r") as file:
        data = json.load(file)
        return data
        

def transaction_format(type_of_op, from_acc, to, amount, direction, old_balance,new_balance):
    
    new_format_transaction = {
        "type": type_of_op,
        "from": from_acc,
        "to": to,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "direction": direction,
        "old_Balance": old_balance,
        "new_balance": new_balance
    }
    return new_format_transaction


#* write all clients again to json (overwrite all prev data)
def save_clients(all_clients_save, filename=DATA_FILE):
    """
        saves client data to data.json database
    """

    # opens the data.json and writes the new data
    with open(filename, "w") as file:
        json.dump(all_clients_save, file, indent=4)

    # print(client_data)

def main():
    print(all_clients())

if __name__ == "__main__":
    main()






