import customtkinter as ctk
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

import models
from ui_windows import test_final_ui
from ui_windows import ui_dashboard
from ui_windows import ui_admin_panel


class AdminLoginScreen(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        #setup
        self.title("Admin secure login")
        self.geometry("400x700")
        self.resizable(False, False)
        self.configure(fg_color = "#0A0E27")
        self.center_window()
        
        # main frame
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.pack(expand=True, fill="both", padx=40)
        
         # logo
        # TODO REPLACE "A" LOGO
        self.logo_label = ctk.CTkLabel(
            self.main_frame, text="A", font=("Inter", 60, "bold"), text_color="#3B82F6")
        self.logo_label.pack(pady=(60, 0))
        
        # bank name
        self.bank_name = ctk.CTkLabel(
            self.main_frame, text="ARGUMENT\nCAPITAL", font=("Inter", 24, "bold"), text_color="white")
        self.bank_name.pack(pady=(0, 0))
        
        # admin login header
        self.main_header = ctk.CTkLabel(
            self.main_frame, 
            text="Admin Login",
            text_color="#EE2626", 
            font=("Inter", 30, "bold"))
        self.main_header.pack(pady=(40, 40))

        # admin ID input field
        self.admin_id_entry = ctk.CTkEntry(
            self.main_frame,
            placeholder_text="Admin ID",
            height=55,
            fg_color="#161C30",
            border_color="#90D5FF",
            text_color="white",
            corner_radius=12
        )
        self.admin_id_entry.pack(fill="x", pady=10)
        
        # password input field
        self.admin_password_entry = ctk.CTkEntry(
            self.main_frame,
            placeholder_text="Admin PIN",
            show="*", # hides input
            height=55,
            fg_color="#161C30",
            border_color="#90d5ff",
            text_color="white",
            corner_radius=12
        )
        self.admin_password_entry.pack(fill="x", pady=10)
        
        # login button
        # TODO logic
        self.admin_login_btn = ctk.CTkButton(
            self.main_frame,
            text="Log In",
            height=55,
            fg_color="#EE2626",
            hover_color="#CA1107",
            font=("Inter", 16, "bold"),
            corner_radius=12,
            command=self.authenticate
        )
        self.admin_login_btn.pack(fill="x", pady=10)
        
        # OR text seperating login or admin login
        self.or_label = ctk.CTkLabel(
            self.main_frame, text="────────  OR  ────────", text_color="#2B344B", font=("Inter", 12))
        self.or_label.pack(pady=20)

        # back to regular Login Link
        self.normal_btn = ctk.CTkButton(
            self.main_frame,
            text="Customer Login",
            fg_color="transparent",
            hover_color="#161C30",
            text_color="#555E70",
            font=("Inter", 13),
            height=40,
            command=self.login_screen
        )
        self.normal_btn.pack(pady=(10, 0))

    def login_screen(self):
        self.destroy()
        reg_login = test_final_ui.LoginScreen()
        reg_login.mainloop()

    def center_window(self):
        self.update_idletasks()
        
        # Get window dimensions
        width = self.winfo_width()
        height = self.winfo_height()
        
        # Get screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        # Calculate coordinates
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        
        # Set the geometry
        self.geometry(f"{width}x{height}+{x}+{y}")

    def popup_win(self,title, message):
        popup_win = ctk.CTkToplevel(self)
        popup_win.title(title)
        popup_win.geometry("300x150")
        popup_win.configure(fg_color="#0A0E27")
        popup_win.resizable(False, False)
        popup_win.attributes("-topmost", True)
        popup_win.grab_set() 


        popup_label = ctk.CTkLabel(popup_win, text=message, font=("Inter", 13), wraplength=250, text_color="white")
        popup_label.pack(pady=20)

        ok_btn = ctk.CTkButton(
            popup_win,
            text="OK", 
            width=100, 
            command=popup_win.destroy,
            fg_color="#3B82F6",
            text_color="white"
        )
        ok_btn.pack(pady=10)
    
        self.center_window(popup_win)

#! //////////////////////////////////////////////////////////////////////
    def authenticate(self):
        admin_id = self.admin_id_entry.get()
        admin_pin = self.admin_password_entry.get()


        if models.Admin.check_admin_login(admin_id, admin_pin):
            self.withdraw() # hides the window!
            
            admin_dash = ui_admin_panel.AdminPanel(admin_id, parent_login=self)
            admin_dash.mainloop()
        else:
            # maybe use popup window with tony's changes! #* imorted my window to here, cant import this function...
            self.popup_win("ERROR" , "incorrect Admin credential's")

#! //////////////////////////////////////////////////////////////////////

            
def main():
    app = AdminLoginScreen()
    app.mainloop()
    
            

if __name__ == "__main__":
    main()