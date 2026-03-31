import storage
import models
import ui_windows.ui_login
import ui_windows.ui_admin_login 
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
        clients = {}
        for client_ID, client_data in data.items():
            clients[client_ID] = Client.from_dict(client_ID, client_data)

        return clients
        

    except FileNotFoundError:
        return []



def main():
    app_login_screen = ui_windows.ui_login.LoginScreen()
    app_login_screen.mainloop()



if __name__ == "__main__":
    main()


