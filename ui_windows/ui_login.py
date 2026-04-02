import customtkinter as ctk
from ui_windows.ui_dashboard import *
from ui_windows.ui_admin_login import *

class LoginScreen(ctk.CTk):
    def __init__(self):
        super().__init__()

        # setup
        self.title("Argument capital Login") # window title
        self.geometry("400x700") # screensize
        self.resizable(False, False) # Prevent the user from shrinking it manually
        self.update_idletasks() # Force the window to update its "inner math" before showing it
        self.configure(fg_color="#0A0E27") # Background
        self.center_window() # Center the window on the screen

        # Main frame
        self.main_frame = ctk.CTkFrame(
            self, 
            fg_color="transparent")
        self.main_frame.pack(expand=True, fill="both", padx=40) # Padding on the sides of the main frame, so the content doesn't touch the edges of the window

        # logo
        self.logo_label = ctk.CTkLabel(
            self.main_frame, 
            text="A", # TODO REPLACE "A" LOGO WITH ACTUAL LOGO
            font=("Inter", 60, "bold"), 
            text_color="#3B82F6")
        self.logo_label.pack(pady=(60, 0))
        
        # bank name
        self.bank_name = ctk.CTkLabel(
            self.main_frame, 
            text="ARGUMENT\nCAPITAL", 
            font=("Inter", 24, "bold"), 
            text_color="white")
        self.bank_name.pack(pady=(0, 0))
        
        # ATM APP as the assignment dictates
        self.app_name = ctk.CTkLabel(
            self.main_frame, 
            text="----------------\nATM APP", 
            font=("Inter", 24, "bold"), 
            text_color="#3B82F6")
        self.app_name.pack(pady=(0, 40))

        # account ID input field
        self.username_entry = ctk.CTkEntry(
            self.main_frame,
            placeholder_text="Account ID",
            height=55,
            fg_color="#161C30",
            border_color="#90D5FF",
            text_color="white",
            corner_radius=12
        )
        self.username_entry.pack(fill="x", pady=10)
        
        # password input field
        self.password_entry = ctk.CTkEntry(
            self.main_frame,
            placeholder_text="PIN",
            show="*", # hides input
            height=55,
            fg_color="#161C30",
            border_color="#90d5ff",
            text_color="white",
            corner_radius=12
        )
        self.password_entry.pack(fill="x", pady=10)

        # password reset button
        self.forgot_btn = ctk.CTkButton(
            self.main_frame,
            text="Change PIN",
            fg_color="transparent",
            hover=False,
            text_color="#555E70",
            font=("Inter", 12),
            width=10
            # TODO connect to change pin screen with command=
        )
        self.forgot_btn.pack(anchor="e", pady=(0, 20))

        # login button
        self.login_btn = ctk.CTkButton(
            self.main_frame,
            text="Log In",
            height=55,
            fg_color="#3B82F6",
            hover_color="#2563EB",
            font=("Inter", 16, "bold"),
            corner_radius=12,
            command= self.open_dashboard # TODO connect to authenticate function
        )
        self.login_btn.pack(fill="x", pady=10)

        # OR text seperating login or admin login
        self.or_label = ctk.CTkLabel(
            self.main_frame, 
            text="────────  OR  ────────", 
            text_color="#2B344B", 
            font=("Inter", 12))
        self.or_label.pack(pady=10)

        #Admin Login Link
        self.admin_btn = ctk.CTkButton(
            self.main_frame,
            text="🛡️ Admin Login",
            fg_color="transparent",
            hover_color="#161C30",
            text_color="#555E70",
            font=("Inter", 13),
            height=40,
            command=self.open_admin_login # open admin login screen and close current login screen
        )
        self.admin_btn.pack(pady=(0))

    # ===========================================================================

    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()# Get window dimensions
        height = self.winfo_height()      
        screen_width = self.winfo_screenwidth()# Get screen dimensions
        screen_height = self.winfo_screenheight() 
        x = (screen_width // 2) - (width // 2) # Calculate coordinates
        y = (screen_height // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}") # Set the geometry
    
    #open dashboard and close login screen
    def open_dashboard(self):
        client_id = self.username_entry.get()
        #add Client.check_pin 
        

        self.destroy()
        dashboard = Dashboard()
        dashboard.mainloop()
    
    #open admin login screen and close current login screen
    def open_admin_login(self):
        self.destroy()
        admin_login = AdminLoginScreen()
        admin_login.mainloop()

# ! todo add authenticate functionality and connect user dashboard screen (like bank acc info)
# ! should work not sure need to test

    # def authenticate(self):

    #     # if id and pin correct -> close window and open new dashboard window
    #     if authenticate:

    #         self.withdraw()  #hide window (don't destroy)
    #         user_dashboard = Dashboard(parent_login=self)

if __name__ == "__main__":
    app = LoginScreen()
    app.mainloop()