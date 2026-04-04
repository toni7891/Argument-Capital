
from PIL import Image, ImageTk
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
    def __init__(self, parent_login=None):
        super().__init__()
 
        self.parent_login = parent_login
        self.title("Users Table For Admins")
        self.geometry("1100x700")
        self.configure(fg_color = "#0A0E27")
        self.resizable(False, False)
        self.center_window()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(script_dir, "ArgumentLogo.ico") 

        # if os.path.exists(icon_path):
        #     img = Image.open(icon_path)
        #     self.photo_icon = ImageTk.PhotoImage(img)
        #     self.wm_iconphoto(False, self.photo_icon)
        #     print(f"Success! Loaded icon from: {icon_path}")
        # else:
        #     print(f"STILL NOT FOUND! Python is looking here: {icon_path}")  
        
        
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
        self.subtitle.pack(side="top")
        
        self.refresh_button = ctk.CTkButton(
            self, 
            text="Refresh Table", 
            command=self.update_table, 
            fg_color="#3B82F6",
            hover_color="#2563EB"
        )
        # self.refresh_button.pack(pady=10, side="top")
        self.refresh_button.place(x=20, y=200)
        
        self.search_label = ctk.CTkLabel(
                self,
                text="Search By Name Or ID: ",
                font=("Verdana", 14, "bold"),
                text_color="white"
            )
        self.search_label.pack()
        
        
        self.search_var = ctk.StringVar()
        self.search_entry = ctk.CTkEntry(
            self,
            corner_radius=10,
            fg_color="#1F1F1F",
            text_color="white", 
            textvariable=self.search_var,
            width=300
        )
        self.search_entry.pack()
        # This triggers the search function every time the user types
        self.search_var.trace_add("write", lambda *args: self.filter_table())
                

        self.scroll_frame = ctk.CTkScrollableFrame(
            master=self,
            width=1000,
            height=500,
            fg_color="#000000"
            )
        
        self.scroll_frame.pack(pady=20, padx=20)
        
        value = self.load_json_data()
        
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
        
    def load_json_data(self):
        try:
            
            data = storage.all_clients()
            print(f"DEBUG: Loaded {len(data)} clients from JSON")
            # print(data) # For debugging
            
            table_data = [["ID", "Username", "Balance", "Blocked Or Active", "Admin Or Client"]]
            
            # user_info is the inner dictionary with username, pin, etc.
            for client_id, user_info in data.items():
                        status = "Blocked" if user_info.get("blocked_or_not") else "Active"
                        acc_type = "Admin" if user_info.get("is_admin") else "Client"
                        
                        row = [
                            client_id,
                            user_info.get("username", "N/A"),
                            f"₪{user_info.get('balance', 0):,.2f}",
                            status,
                            acc_type
                        ]
                        table_data.append(row)
            return table_data
        except Exception as e:
                return [["Error"], [str(e)]]
    
    def on_closing(self):
        if self.parent_login:
            self.parent_login.deiconify()
        self.destroy()
        
    
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


            
    def update_table(self):
        try:
            new_values = self.load_json_data()
            self.table.configure(values=new_values) # Update the table widget with the new list of lists
        
            # print("Table updated successfully!")
        
        except Exception as e:
            return e
        
    def filter_table(self):
        search_term = self.search_var.get().lower()
        
        full_data = self.load_json_data()
        header = full_data[0]
        
        filtered_data = [header]
        for row in full_data[1:]:
            if search_term in str(row[0]).lower() or search_term in str(row[1]).lower():
                filtered_data.append(row)
                
        if len(filtered_data) == 1:
            filtered_data.append(["-", "No results found", "-", "-", "-"])
        
        # force the table to update fix
        self.table.configure(rows=len(filtered_data), values=filtered_data)
        # self.table.pack(expand=True, fill="both")
        # self.table.update()
        self.scroll_frame._parent_canvas.yview_moveto(0) 
        self.update_idletasks()
                

    
def main():
    user_table = Admin_user_table()
    user_table.mainloop()
    
      
    
if __name__ == "__main__":
    main()