
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


        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(expand=True, fill="both", padx=40)

        # Create Account Button
        self.create_btn = self.create_admin_button(
            "Create New Account", 
            self.open_create_account_window
        )
        
        # Accounts Dashboard Button
        self.dash_btn = self.create_admin_button(
            "Accounts Dashboard", 
            self.open_accounts_list
        )
        
        # Block/Unblock Account Button
        self.block_btn = self.create_admin_button(
            "Block/Unblock User", 
            self.open_block_window
        )
        
        # Logout Button
        self.logout_btn = ctk.CTkButton(
            self.button_frame,
            text="Logout",
            height=50,
            corner_radius=10,
            fg_color="transparent",
            border_width=2,
            border_color="#EF4444",
            text_color="#EF4444",
            hover_color="#2D1B1B",
            command=self.logout
        )
        self.logout_btn.pack(fill="x", pady=10)







      
if __name__ == "__main__":
    # Test the panel
    app = AdminPanel("ADMIN01")
    app.mainloop()