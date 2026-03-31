import json
import models

def all_clients(filename="data.json"):
    
    #read the data.json and store client data in data var 
    with open(filename, "r") as file:
        data = json.load(file)

    #making list full of clients (as class object)
    all_clients = models.Client.from_dict(data)
    return all_clients


#* write all clients again to json (overwrite all prev data)
def save_clients(clients, filename="data.json"):
    """
        saves client data to data.json database
    """

    # converts the class type data to dict using the function inside the class (json accepts dict) 
    # than adds to list with all accounts created for further addition to json file
    client_data = []
    for client in clients:
        client_data.append(client.to_dict())

    # opens the data.json and writes the new data
    with open(filename, "w") as file:
        json.dump(client_data, file, indent=4)

    print(client_data)







    """
    output into file:
    [
        {
            "client_ID": "1234567",
            "pin": "1234",
            "balance": 1000
        }
    ]
    """




