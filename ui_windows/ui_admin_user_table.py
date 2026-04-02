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
            corner_radius=60, 
            height=60,
            fg_color="transparent") # TODO add user variable and logic
        self.header_frame.pack_propagate(False)
        self.header_frame.pack(fill="x", padx=5, pady=20)  
        
        #welcome label
        self.header = ctk.CTkLabel(
            self.header_frame,
            text="Users Table:", # TODO add user variable and logic here
            font=("Segoe UI", 60),
            text_color="white"
        )
        self.header.pack(side="top", padx=20) 
        
        
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

        # Creating the table
        table = CTkTable(
            master=self, 
            # row=5, 
            # column=4,
            values=value,
            header_color="#3B8ED0", # Custom header color
            hover_color="#2A2D2E",   # Highlight row on hover
            colors=["#3A6C7D", "#3A6C7D"],
            width=140,   # Smaller width per cell (default is usually 140)
            height=40   # Smaller height per cell (default is usually 28) 
        )
        
        # table.pack(expand=True, padx=20, pady=20)

        scroll_frame = ctk.CTkScrollableFrame(master=self, width=1000, height=500)
        scroll_frame.pack(pady=20, padx=20)
        
        table = CTkTable(master=scroll_frame, values=value)
        table.pack(expand=True, fill="both")  


            
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