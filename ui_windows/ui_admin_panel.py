
import customtkinter as ctk
from PIL import Image, ImageTk
from CTkTable import *
import sys
import os
#?--> use the command if you dont have CTkTable > pip install CTkTable


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

import models
import storage
import json
MAIN_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(MAIN_DIR, "data.json")


class AdminPanel(ctk.CTk):
    def __init__(self, admin_id, parent_login=None):
        super().__init__()
        self.admin_id = admin_id
        self.parent_login = parent_login
        
        
        self.title("Admin Control Center")
        self.geometry("400x600")
        self.configure(fg_color="#0A0E27") 
        self.resizable(False, False)
        
        # Header Section
        self.header_label = ctk.CTkLabel(
            self, 
            text="ADMIN CONTROL PANEL", 
            font=("Inter", 20, "bold"),
            text_color="white"
        )
        self.header_label.pack(pady=(40, 20))









      
if __name__ == "__main__":
    # Test the panel
    app = AdminPanel("ADMIN01")
    app.mainloop()