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


def print_format():




    print (new_from_transaction = storage.transaction_format(type_of_operation, all_clients_trans[trans_from_id]["username"], all_clients_trans[trans_to_id]["username"], -amount, old_balance_from, new_balance_from))

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
