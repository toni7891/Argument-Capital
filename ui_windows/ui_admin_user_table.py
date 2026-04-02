import customtkinter as ctk
from CTkTable import *
#?--> use the command if you dont have CTkTable > pip install CTkTable

class Admin_user_table(ctk.CTk):
    def __init__(self):
        super().__init__()
 
        
        self.title("Users Table For Admins")
        self.geometry("1100x700")
        self.configure(fg_color = "#0A0E27")
        self.resizable(False, False)
        self.center_window()

        self.header_frame = ctk.CTkFrame(
            self, 
            corner_radius=15,        
            height=120,              
            fg_color=("#2B2B2B", "#1A1A1A"),
            border_width=2,
            border_color="#3B8ED0"   
        )
        self.header_frame.pack_propagate(False)
        self.header_frame.pack(fill="x", padx=20, pady=(20)) 
        
        self.header = ctk.CTkLabel(
            master=self.header_frame,
            text="Admin User LookUp",
            # Using 'bold' makes the Segoe UI font look premium
            font=("Segoe UI", 50, "bold"), 
            text_color="#FFFFFF"
        
        )
        self.header.pack(side="top", padx=10, pady=5)
        
        self.subtitle = ctk.CTkLabel(
            self.header_frame,
            text="● Full User Database List ●",
            font=("Segoe UI", 14),
            text_color="#FFFFFF" # Matching blue
        )
        self.subtitle.pack(side="top", padx=5, pady=(0, 0))
        
        
        # Defining the data (Rows and Columns)
        value = [
            ["ID", "Name", "Email", "Status"],
            [1, "Alice Smith", "alice@example.com", "Active"],
            [2, "Bob Johnson", "bob@example.com", "Inactive"],
            [3, "Charlie Brown", "charlie@example.com", "Active"],
            [4, "Charlie Brown", "charlie@example.com", "Active"],
            [5, "Charlie Brown", "charlie@example.com", "Active"],
            [6, "Charlie Brown", "charlie@example.com", "Active"],
            [7, "Charlie Brown", "charlie@example.com", "Active"],
            [8, "Charlie Brown", "charlie@example.com", "Active"],
            [9, "Charlie Brown", "charlie@example.com", "Active"],
            [10, "Charlie Brown", "charlie@example.com", "Active"],
            [11, "Charlie Brown", "charlie@example.com", "Active"],
            [12, "David Wilson", "david@example.com", "Pending"]
        ]
        
        # table.pack(expand=True, padx=20, pady=20)

        self.scroll_frame = ctk.CTkScrollableFrame(
            master=self,
            width=1000,
            height=500,
            fg_color="#0A0E27"
            )
        
        self.scroll_frame.pack(pady=20, padx=20)
        
        
        self.table = CTkTable(
            master=self.scroll_frame,
            corner_radius=10, 
            # row=5, 
            # column=4,
            padx=1,              
            pady=1,               
            fg_color="#000000",   
            values=value,
            header_color="#3B8ED0", 
            hover_color="#2A2D2E",   
            colors=["#3A6C7D", "#3A6C7D"],
            width=140,  
            height=40    
        )
        
        self.table.pack(expand=True, fill="both")  
        
    

            
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
    
    
def main():
    user_table = Admin_user_table()
    user_table.mainloop()
      
    
if __name__ == "__main__":
    main()