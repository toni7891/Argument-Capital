
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
        self.center_window()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.title("Admin Control Center")
        self.geometry("400x700")
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

    def on_closing(self):
            if self.parent_login:
                self.parent_login.destroy() # Kills the hidden login window too
            self.destroy()

    def center_window(self, window=None):
        
        win = window if window else self
    
        win.update_idletasks()
    
        width = win.winfo_width()
        height = win.winfo_height()
    
        # get screen dimensions
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
    
        # calculate coordinates
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
    
        win.geometry(f"{width}x{height}+{x}+{y}")


    def create_admin_button(self, text, command):
            btn = ctk.CTkButton(
                self.button_frame,
                text=text,
                height=60,
                corner_radius=10,
                fg_color="#3B82F6",
                hover_color="#2563EB",
                text_color="white",
                font=("Inter", 14, "bold"),
                command=command
            )
            btn.pack(fill="x", pady=10)
            return btn

    def create_account_logic(self, create_win, user_entry, pin_entry, bal_entry, is_admin_var):
            try:
                username = user_entry.get()
                pin = pin_entry.get()
                balance_str = bal_entry.get()
                is_admin = is_admin_var.get()

                if not username or not pin or not balance_str:
                    self.popup_win("Error", "All fields are required!")
                    return
                
                balance = float(balance_str)

                models.Admin.create_client_account(
                    username=username, 
                    pin=pin, 
                    balance=balance, 
                    blocked_or_not=False, 
                    is_admin=is_admin
                )

                self.popup_win("Success", f"{'Admin' if is_admin else 'User'} account created!")
                create_win.destroy()

            except ValueError:
                self.popup_win("Error", "Balance must be a number.")


    def open_create_account_window(self):
            create_win = ctk.CTkToplevel(self)
            create_win.title("Create New Account")
            create_win.geometry("400x550")
            create_win.configure(fg_color="#0A0E27")
            create_win.attributes('-topmost', True)
            create_win.grab_set()
            create_win.resizable(False, False)

            frame = ctk.CTkFrame(create_win, fg_color="transparent")
            frame.pack(expand=True, fill="both", padx=40, pady=20)

            ctk.CTkLabel(frame, text="Create New User", font=("Inter", 20, "bold"), text_color="white").pack(pady=20)

            user_entry = ctk.CTkEntry(frame, placeholder_text="Username", height=45, corner_radius=10)
            user_entry.pack(fill="x", pady=10)

            pin_entry = ctk.CTkEntry(frame, placeholder_text="PIN (4 digits)", height=45, corner_radius=10)
            pin_entry.pack(fill="x", pady=10)

            bal_entry = ctk.CTkEntry(frame, placeholder_text="Initial Balance", height=45, corner_radius=10)
            bal_entry.pack(fill="x", pady=10)

            is_admin_var = ctk.BooleanVar(value=False)
            admin_switch = ctk.CTkSwitch(
                frame, 
                text="Give Admin Privileges", 
                variable=is_admin_var,
                progress_color="#EE2626",
                font=("Inter", 13),
                text_color="white"
            )
            admin_switch.pack(pady=20)

            confirm_btn = ctk.CTkButton(
                frame, 
                text="Create Account", 
                height=50, 
                fg_color="#3B82F6",
                command=lambda: self.create_account_logic(
                    create_win, user_entry, pin_entry, bal_entry, is_admin_var
                )
            )
            confirm_btn.pack(fill="x", pady=(10, 10))

            ctk.CTkButton(frame, text="Cancel", fg_color="#1F1F1F", command=create_win.destroy).pack(fill="x")
            
            self.center_window(create_win)

    def open_accounts_list(self):
        print("Opening Global Accounts Table...")

    def open_block_window(self):
        print("Opening Blocking Interface...")

    def logout(self):
        if self.parent_login:
            self.parent_login.deiconify() #--> this opens back the window we closed with withdraw() in ui_admin_panel.
        self.destroy()



      
if __name__ == "__main__":
    app = AdminPanel("ADMIN01")
    app.mainloop()