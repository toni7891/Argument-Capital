import customtkinter as ctk
from ui_windows.ui_dashboard import *

class LoginScreen(ctk.CTk):
    def __init__(self):
        super().__init__()

        # setup
        self.title("Argument capital Login")
        self.geometry("400x700")
        self.configure(fg_color="#0A0E27")  # Background

        # Main frame
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
        
        # ATM APP as the assignment dictates
        self.app_name = ctk.CTkLabel(
            self.main_frame, text="----------------\nATM APP", font=("Inter", 24, "bold"), text_color="#3B82F6")
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
        # TODO logic
        self.forgot_btn = ctk.CTkButton(
            self.main_frame,
            text="Change PIN",
            fg_color="transparent",
            hover=False,
            text_color="#555E70",
            font=("Inter", 12),
            width=10
        )
        self.forgot_btn.pack(anchor="e", pady=(0, 20))

        # login button
        # TODO login button logic transfering to dashboard
        self.login_btn = ctk.CTkButton(
            self.main_frame,
            text="Log In",
            height=55,
            fg_color="#3B82F6",
            hover_color="#2563EB",
            font=("Inter", 16, "bold"),
            corner_radius=12,
            # command= TBA
        )
        self.login_btn.pack(fill="x", pady=10)

        # OR text seperating login or admin login
        self.or_label = ctk.CTkLabel(
            self.main_frame, text="────────  OR  ────────", text_color="#2B344B", font=("Inter", 12))
        self.or_label.pack(pady=20)

        # Admin Login Link
        self.admin_btn = ctk.CTkButton(
            self.main_frame,
            text="🛡️ Admin Login",
            fg_color="transparent",
            hover_color="#161C30",
            text_color="#555E70",
            font=("Inter", 13),
            height=40,
            # command= TBA
        )
        self.admin_btn.pack(pady=(10, 0))   

    # ! todo add authenticate functionality and connect user dashboard screen (like bank acc info)
    # ! should work not sure need to test

    def authenticate(self):

        # if id and pin correct -> close window and open new dashboard window
        if authenticate:

            self.destroy()  #close window
            user_dashboard = Dashboard() 
            user_dashboard.mainloop()

if __name__ == "__main__":
    app = LoginScreen()
    app.mainloop()