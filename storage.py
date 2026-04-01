import json
import models

def all_clients(filename="data.json"):
    
    #read the data.json and store client data in data var 
    with open(filename, "r") as file:
        data = json.load(file)
        return data


#* write all clients again to json (overwrite all prev data)
def save_clients(all_clients_save, filename="data.json"):
    """
        saves client data to data.json database
    """

    # opens the data.json and writes the new data
    with open(filename, "w") as file:
        json.dump(all_clients_save, file, indent=4)

    # print(client_data)


# def main():
#     #all_clients()

# if __name__ == "__main__":
#     main()




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




