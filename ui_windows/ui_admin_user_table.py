
import customtkinter as ctk
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
            border_color="#3B82F6"   
        )
        self.header_frame.pack_propagate(False)
        self.header_frame.pack(fill="x", padx=20, pady=(20)) 
        
        title_font = ctk.CTkFont(family="Verdana", size=60, weight="bold")
        
        self.header = ctk.CTkLabel(
            master=self.header_frame,
            text="Admin User LookUp",
            font=title_font, 
            text_color="#FFFFFF"
        )
        self.header.pack(side="top", padx=10, pady=5)
        
        self.subtitle = ctk.CTkLabel(
            self.header_frame,
            text="● Full User Database List ●",
            font=("Verdana", 14),
            text_color="#FFFFFF" 
        )
        self.subtitle.pack(side="top", padx=5, pady=(0, 0))
        
        
        
        # Defining the data (Rows and Columns)
        value = self.load_json_data()
        
        # table.pack(expand=True, padx=20, pady=20)

        self.scroll_frame = ctk.CTkScrollableFrame(
            master=self,
            width=1000,
            height=500,
            fg_color="#000000"
            )
        
        self.scroll_frame.pack(pady=20, padx=20)
        
        
        self.table = CTkTable(
            master=self.scroll_frame,
            corner_radius=10,
            font=("Verdana", 12, "bold"), 
            # row=5, 
            # column=4,
            padx=1,              
            pady=1,               
            fg_color="#C9C9C9",   
            values=value,
            header_color="#3B82F6", 
            hover_color="#2A2D2E",   
            colors=["#3A6C7D", "#3A6C7D"],
            width=140,  
            height=40,
            text_color="#DBDBDB"    
        )
        
        self.table.pack(expand=True, fill="both")
        
        
        # for row_idx, row_data in enumerate(self.load_json_data()):
        #     if row_idx == 0: continue # Skip header
            
        #     # If the status is "Blocked", make the text Red
        #     if "Blocked" in row_data[3]:
        #         self.table.insert(row_idx, 3, text_color="#E74C3C")
        #     else:
        #         self.table.insert(row_idx, 3, text_color="#2ECC71") # Green for Active  
                
        # # self.table.pack(expand=True, fill="both")
        
    def center_window(self, window=None):
       
        win = window if window else self
    
        win.update_idletasks()
    
        
        width = win.winfo_width()
        height = win.winfo_height()
    
        
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
    
        # Calculate coordinates
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
    
        # Apply to the correct window
        win.geometry(f"{width}x{height}+{x}+{y}")


    def load_json_data(self):
        try:
            # Get the dictionary from your storage logic
            data = storage.all_clients()
            print(data) # For debugging
            
            
            table_data = [["ID", "Username", "Pin", "Balance", "Blocked_Or_Not", "is_admin", "ButtonForTransactions"]]
            
            # user_info is the inner dictionary with username, pin, etc.
            for client_id, user_info in data.items():
                        status = "Blocked" if user_info.get("blocked_or_not") else "Active"
                        acc_type = "Admin" if user_info.get("is_admin") else "Client"
                        
                        row = [
                            client_id,
                            user_info.get("username", "N/A"),
                            f"${user_info.get('balance', 0):,.2f}",
                            status,
                            acc_type
                        ]
                        table_data.append(row)
            return table_data
        except Exception as e:
                return [["Error"], [str(e)]]

        #     for client_id, user_info in data.items():
                
        #         # Determine status string
        #         status = "Blocked" if user_info.get("blocked_or_not") else "Active"
                
        #         # Determine account type string
        #         acc_type = "Admin" if user_info.get("is_admin") else "Client"
                
        #         # Create the row
        #         row = [
        #             client_id,                                # The key from JSON
        #             user_info.get("username", "N/A"),         # tony, guy, etc.
        #             f"${user_info.get('balance', 0):,.2f}",    # Formatted balance
        #             status,
        #             acc_type
        #         ]
        #         table_data.append(row)
                
        #     return table_data

        # except (FileNotFoundError, json.JSONDecodeError):
        #     return [["Error"], ["Could not load data.json"]]
        


    
def main():
    user_table = Admin_user_table()
    user_table.mainloop()
    # print(Admin_user_table.load_json_data())
    
      
    
if __name__ == "__main__":
    main()