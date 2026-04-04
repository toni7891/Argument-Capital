import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)


import storage
import models
from ui_windows import test_final_ui
from ui_windows import ui_dashboard
from ui_windows import ui_admin_login

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
            clients[client_ID] = models.Client.from_dict(client_ID, client_data)

        return clients
        

    except FileNotFoundError:
        return []



def main():
    app_login_screen = test_final_ui.LoginScreen()
    app_login_screen.mainloop()

if __name__ == "__main__":
    main()


