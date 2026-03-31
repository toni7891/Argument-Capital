from storage import *
from models import *


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
        return [
            for item in data:
                Client.from_dict(item)
        ]

    except FileNotFoundError:
        return []



def main():
    var = None



if __name__ == "__main__":
    main()


