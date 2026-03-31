from storage import *
from models import *
import json


# ! THIS IS THE MAIN.PY FILE


def load_clients(filename="data.json"):
    """
        show all clients for admin dashboard
    """

    try:
        #read the data.json and store client data in data var 
        with open(filename, "r") as file:
            data = json.load(file)

        # return data in class type from dict in which its stored in json file.
        clients = []
        for item in data:
            client_object = Client.from_dict(item)
            clients.append(client_object)

        return clients
        

    except FileNotFoundError:
        return []



def main():
    var = None



if __name__ == "__main__":
    main()


