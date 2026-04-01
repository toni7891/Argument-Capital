
def all_clients(filename="data.json"):
        with open(filename, "r") as file:
        data = json.load(file)
    return data




def main():
    print(all_clients())




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
