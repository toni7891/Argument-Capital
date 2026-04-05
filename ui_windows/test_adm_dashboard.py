import customtkinter as ctk
from CTkTable import *
import os
import sys

# Standard path setup for your project structure
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

import storage # Assuming storage.all_clients() returns your JSON dict

class Admin_user_table(ctk.CTkToplevel):
    def __init__(self, parent_login=None):
        super().__init__()
 
        self.parent_login = parent_login
        self.title("Users Table For Admins")
        self.geometry("1100x700")
        self.configure(fg_color="#0A0E27")
        self.resizable(False, False)
        
        # 1. UI Setup (Header, Search Bar, etc.)
        self.setup_ui()

        # 2. Data Initialization
        # We store the 'master_data' in memory so searching is instant
        self.master_data = self.load_json_data()
        
        # 3. Table Creation
        self.scroll_frame = ctk.CTkScrollableFrame(self, width=1000, height=500, fg_color="#000000")
        self.scroll_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        self.table = CTkTable(
            master=self.scroll_frame,
            values=self.master_data,
            colors=["#3A6C7D", "#3A6C7D"],
            header_color="#3B82F6",
            hover_color="#2A2D2E",
            text_color="#DBDBDB",
            width=140,
            height=40
        )
        self.table.pack(expand=True, fill="both")

        # 4. The Trace (Search Listener)
        # CRITICAL: No parentheses after filter_table! 
        # Placed at the end to ensure self.table exists.
        self.search_var.trace_add("write", self.filter_table)
        
        self.update_idletasks()

    def setup_ui(self):
        # Header
        self.header_frame = ctk.CTkFrame(self, height=100, fg_color=("#2B2B2B", "#1A1A1A"))
        self.header_frame.pack(fill="x", padx=20, pady=20)
        
        ctk.CTkLabel(self.header_frame, text="Admin User LookUp", font=("Verdana", 40, "bold")).pack()
        
        # Search Section
        self.search_var = ctk.StringVar()
        self.search_entry = ctk.CTkEntry(self, placeholder_text="Search Name or ID...", 
                                        textvariable=self.search_var, width=300)
        self.search_entry.pack(pady=10)

    def load_json_data(self):
        """ Parses your specific JSON format into a list of lists for CTkTable """
        try:
            # data = { "100": {"username": "tony", ...}, "101": {...} }
            data = storage.all_clients() 
            
            table_headers = ["ID", "Username", "Balance", "Status", "Account Type"]
            rows = [table_headers]
            
            for client_id, info in data.items():
                # Formatting data for the table
                status = "Blocked" if info.get("blocked_or_not") else "Active"
                role = "Admin" if info.get("is_admin") else "Client"
                balance = f"₪{info.get('balance', 0):,.2f}"
                
                row = [
                    client_id, 
                    info.get("username", "N/A"), 
                    balance, 
                    status, 
                    role
                ]
                rows.append(row)
            return rows
        except Exception as e:
            print(f"Error loading JSON: {e}")
            return [["Error"], [str(e)]]

    def filter_table(self, *args):
        """ Filters the existing master_data list based on search input """
        if not hasattr(self, 'table'):
            return

        search_term = self.search_var.get().lower()
        header = self.master_data[0]
        filtered_data = [header]

        # Search through IDs and Usernames
        for row in self.master_data[1:]:
            # row[0] is ID, row[1] is Username
            if search_term in str(row[0]).lower() or search_term in str(row[1]).lower():
                filtered_data.append(row)
        
        if len(filtered_data) == 1 and search_term != "":
            filtered_data.append(["-", "No results found", "-", "-", "-"])

        # Update the table widget
        self.table.configure(values=filtered_data, rows=len(filtered_data))

def main():
    root = ctk.CTk()
    root.withdraw()
    user_table = Admin_user_table(parent_login=root)
    root.mainloop()

if __name__ == "__main__":
    main()