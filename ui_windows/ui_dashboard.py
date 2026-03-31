import customtkinter as ctk

class Dashboard(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        #setup
        self.title("Dashboard")
        self.geometry("400x700")
        self.configure(fg_color = "#0A0E27")
        
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
            # TODO add logic
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
            # TODO add logic
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
            # TODO add logic
        )
        self.logout_button.grid(row=2, column=1, padx=10, pady=10)
  
if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()