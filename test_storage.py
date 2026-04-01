import json
import models

def all_clients(filename="data.json"):
        with open(filename, "r") as file:
            data = json.load(file)
            return data
        # print(data)


def find_client_data(data_from):
    for client_id, info in data_from.items():
        print(client_id)
        print(info)



def main():
    # print(type(all_clients()))
    all_clients_data = all_clients()
    find_client_data(all_clients_data)



if __name__ == "__main__":
    main()


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
