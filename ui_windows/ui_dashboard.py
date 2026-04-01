import customtkinter as ctk

class Dashboard(ctk.CTk):
    def __init__(self, parent_login=None):
        super().__init__()
        self.parent_login = parent_login
        
        #setup
        self.title("Dashboard")
        self.geometry("400x700")
        self.configure(fg_color = "#0A0E27")
        self.resizable(False, False)
        self.center_window()
        
        #welcome frame
        self.welcome_frame = ctk.CTkFrame(
            self, 
            corner_radius=20, 
            height=20,
            fg_color="transparent") # TODO add user variable and logic
        self.welcome_frame.pack_propagate(False)
        self.welcome_frame.pack(fill="x", padx=5, pady=20)  
        
        #welcome label
        self.welcome = ctk.CTkLabel(
            self.welcome_frame,
            text="Welcome 'User'", # TODO add user variable and logic here
            font=("Inter", 14),
            text_color="white"
        )
        self.welcome.pack(side="left", padx=20)

        #top frame
        self.top_frame = ctk.CTkFrame(
            self, 
            corner_radius=20, 
            height=100, 
            fg_color="#3B82F6")
        self.top_frame.pack_propagate(False)
        self.top_frame.pack(fill="x", padx=20, pady=10)
        
        #balance title
        self.balance_title = ctk.CTkLabel(
            self.top_frame,
            text="Current Balance",
            font=("Inter", 12),      # Smaller font for the title
            text_color="lightgray"   # Different color for hierarchy
        )
        self.balance_title.pack(side="top", anchor="w", padx=20, pady=(10, 0))
        
        #balance itself
        self.balance_label = ctk.CTkLabel(
            self.top_frame,
            text="'₪25,000'", # TODO balance amount variable here <-
            font=("Inter", 40),
            text_color="white"
        )
        self.balance_label.pack(side="bottom", anchor="w", padx=20, pady=(0, 20))  
              
        #placeholder frame
        self.ph_frame = ctk.CTkFrame(
            self,
            fg_color="transparent",
            # border_color="transparent",
            # border_width=2,
            height=40
        )
        self.ph_frame.pack(
            expand=True, 
            fill="both", 
            padx=20,
        )
              
        #actions frame
        self.main_frame = ctk.CTkFrame(
            self, 
            fg_color="transparent"
            # border_color="transparent",
            # border_width=2
        )
        self.main_frame.pack(
            expand=True, 
            fill="both", 
            padx=20,
            pady=(10, 40))
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        
        #row 0
        self.transfer_button = ctk.CTkButton(
            self.main_frame, 
            text="Transfer Funds", 
            width=170,             
            height=80,             
            corner_radius=10,       
            fg_color="transparent", 
            border_width=2,         
            border_color="white",
            text_color="white",     
            font=("Inter", 14),   
            hover_color="#1F1F1F", 
            # TODO add logic
        )
        self.transfer_button.grid(row=0, column=0, padx=10, pady=10)
        
        self.change_pin_button = ctk.CTkButton(
            self.main_frame, 
            text="Change pin", 
            width=170,              
            height=80,             
            corner_radius=10,        
            fg_color="transparent", 
            border_width=2,         
            border_color="white",
            text_color="white",               
            font=("Inter", 14),           
            hover_color="#1F1F1F", 
            # TODO add pin change logic
        )
        self.change_pin_button.grid(row=0, column=1, padx=10, pady=10)
        
        #row 1
        self.deposit_button = ctk.CTkButton(
            self.main_frame, 
            text="Deposit", 
            width=170,             
            height=80,             
            corner_radius=10,       
            fg_color="transparent", 
            border_width=2,         
            border_color="white",
            text_color="white",     
            font=("Inter", 14),   
            hover_color="#1F1F1F", 
            command=self.open_window
        )
        self.deposit_button.grid(row=1, column=0, padx=10, pady=10)
        
        self.withdraw_button = ctk.CTkButton(
            self.main_frame, 
            text="withdraw", 
            width=170,             
            height=80,             
            corner_radius=10,       
            fg_color="transparent", 
            border_width=2,         
            border_color="white",
            text_color="white",     
            font=("Inter", 14),   
            hover_color="#1F1F1F", 
            command=self.open_withdraw_window
        )
        self.withdraw_button.grid(row=1, column=1, padx=10, pady=10)
        
        # row 2
        self.statements_button = ctk.CTkButton(
            self.main_frame, 
            text="View\nStatements", 
            width=170,             
            height=80,             
            corner_radius=10,       
            fg_color="transparent", 
            border_width=2,         
            border_color="white",
            text_color="white",     
            font=("Inter", 14),   
            hover_color="#1F1F1F", 
            # TODO add logic
        )
        self.statements_button.grid(row=2, column=0, padx=10, pady=10)
        
        self.logout_button = ctk.CTkButton(
            self.main_frame, 
            text="Logout", 
            width=170,             
            height=80,             
            corner_radius=10,       
            fg_color="transparent", 
            border_width=2,         
            border_color="white",
            text_color="white",     
            font=("Inter", 14),   
            hover_color="#1F1F1F", 
            command=self.logout
        )
        self.logout_button.grid(row=2, column=1, padx=10, pady=10)
    
    #center window function that can be used for any window (main or toplevel)
    def center_window(self, window=None):
        # If no window is provided, use 'self' (the main window)
        win = window if window else self
    
        win.update_idletasks()
    
         # Get dimensions of the specific window
        width = win.winfo_width()
        height = win.winfo_height()
    
        # Get screen dimensions
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
    
        # Calculate coordinates
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
    
        # Apply to the correct window
        win.geometry(f"{width}x{height}+{x}+{y}")
    #open deposit window
    def open_window(self):
            dep_win = ctk.CTkToplevel(self)
            dep_win.title("Deposit")
            dep_win.geometry("400x400")
            dep_win.configure(fg_color="#0A0E27")
            dep_win.resizable(False, False)
            
            #frame
            dep_win.frame = ctk.CTkFrame(
                dep_win, 
                corner_radius=20, 
                fg_color="#0A0E27")
            dep_win.frame.pack(expand=True, fill="both", padx=20, pady=20)
            
            #label
            dep_win.dep = ctk.CTkLabel(
                dep_win.frame,
                text="Deposit Funds",
                font=("Inter", 16, "bold"),
                text_color="white"
            )
            dep_win.dep.pack(pady=20)
            
            #entry
            dep_win.amount_entry = ctk.CTkEntry(
                dep_win.frame,
                placeholder_text="Enter amount to deposit",
                font=("Inter", 14),
                width=300,
                height=40,
                corner_radius=10,
                fg_color="#1F1F1F",
                text_color="white",
                border_width=0
            )
            dep_win.amount_entry.pack(pady=10)
            self.center_window(dep_win)
            
            #confirm button
            dep_win.confirm_btn = ctk.CTkButton(
                dep_win.frame,
                text="Confirm Deposit",
                width=300,
                height=40,
                corner_radius=10,
                fg_color="#3B82F6",
                hover_color="#2563EB",
                font=("Inter", 14, "bold"),
                # TODO add logic
            )
            dep_win.confirm_btn.pack(pady=(30, 10))
            
            #cancel button
            dep_win.cancel_btn = ctk.CTkButton(
                dep_win.frame,
                text="Cancel",
                width=300,
                height=40,
                corner_radius=10,
                fg_color="#1F1F1F",
                hover_color="#3B3B3B",
                font=("Inter", 14, "bold"),
                command=lambda: self.close_window(dep_win)
            )
            dep_win.cancel_btn.pack(pady=0)
    #open withdraw window
    def open_withdraw_window(self):
            with_win = ctk.CTkToplevel(self)
            with_win.title("Withdraw")
            with_win.geometry("400x400")
            with_win.configure(fg_color="#0A0E27")
            with_win.resizable(False, False)
            
            #frame
            with_win.frame = ctk.CTkFrame(
                with_win, 
                corner_radius=20, 
                fg_color="#0A0E27")
            with_win.frame.pack(expand=True, fill="both", padx=20, pady=20)
            
            #label
            with_win.with_label = ctk.CTkLabel(
                with_win.frame,
                text="Withdraw Funds",
                font=("Inter", 16, "bold"),
                text_color="white"
            )
            with_win.with_label.pack(pady=20)
            
            #entry
            with_win.amount_entry = ctk.CTkEntry(
                with_win.frame,
                placeholder_text="Enter amount to withdraw",
                font=("Inter", 14),
                width=300,
                height=40,
                corner_radius=10,
                fg_color="#1F1F1F",
                text_color="white",
                border_width=0
            )
            with_win.amount_entry.pack(pady=10)
            
            #confirm button
            with_win.confirm_btn = ctk.CTkButton(
                with_win.frame,
                text="Confirm Withdraw",
                width=300,
                height=40,
                corner_radius=10,
                fg_color="#3B82F6",
                hover_color="#2563EB",
                font=("Inter", 14, "bold"),
                # TODO add logic
            )
            with_win.confirm_btn.pack(pady=(30, 10))
            
            #cancel button
            with_win.cancel_btn = ctk.CTkButton(
                with_win.frame,
                text="Cancel",
                width=300,
                height=40,
                corner_radius=10,
                fg_color="#1F1F1F",
                hover_color="#3B3B3B",
                font=("Inter", 14, "bold"),
                command=lambda: self.close_window(with_win)
            )
            with_win.cancel_btn.pack(pady=0)
            self.center_window(with_win)
    #logs out and returns to login window
    def logout(self):
        self.destroy()
        if self.parent_login:
            self.parent_login.deiconify()
    #open change pin window
    def change_pin_window(self):
        pass 
        
    #TODO add confirm logic for deposit and other actions, also add logic for pin change and transfer funds, view statements, and logout
  
    def close_window(self, window):
        window.destroy()
        
if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()