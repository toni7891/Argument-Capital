import json


def save_clients(clients, filename="data.json"):
    """
        saves client data to data.json database
    """

    # converts the class type data to dict using the function inside the class (json accepts dict) 
    # than adds to list with all accounts created for further addition to json file
    client_data = []
    for client in clients:
        data.append(client.to_dict())

    # opens the data.json and writes the new data
    with open(filename, "w") as file:
        json.dump(client_data, file, indent=4)

    """
    output into file:
    [
        {
            "username": "tony",
            "password": "1234",
            "balance": 1000
        }
    ]
    """

    


