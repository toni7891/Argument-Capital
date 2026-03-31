from storage import *
from models import *


# ! THIS IS THE MAIN.PY FILE


def load_clients(filename="data.json"):
    """
        show all clients for admin dashboard
    """

    try:
        with open(filename, "r") as file:
            data = json.load(file)

        return [Client.from_dict(item) for item in data]

    except FileNotFoundError:
        return []



def main():
    var = None



if __name__ == "__main__":
    main()


