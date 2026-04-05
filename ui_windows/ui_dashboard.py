import customtkinter as ctk
from tkinter import ttk
import sys
import os
from PIL import Image
from CTkTable import *

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

import models
import storage
import json



class Dashboard(ctk.CTk):
    def __init__(self, current_client_id, parent_login=None):
        super().__init__()
        self.current_client_id = current_client_id
        self.parent_login = parent_login
        #to prevent the login window to stay alive in case of abrupt closing beacuse login page is withdraw() and not destory()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        
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
            fg_color="transparent")
        self.welcome_frame.pack_propagate(False)
        self.welcome_frame.pack(fill="x", padx=5, pady=20)  
        
        #welcome label
        client_info = models.Admin.find_account(self.current_client_id)
        userid_name = client_info["username"]
        userid_id = self.current_client_id
        self.welcome = ctk.CTkLabel(
            self.welcome_frame,
            text= f"Welcome {userid_name} , ID: {userid_id}",
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
        
        client_info = models.Admin.find_account(self.current_client_id)
        balance_for_real = client_info["balance"]
        
        #balance itself
        self.balance_label = ctk.CTkLabel(
            self.top_frame,
            text=(f"₪{balance_for_real}"),
            font=("Inter", 40),
            text_color="white"
        )
        self.balance_label.pack(side="bottom", anchor="w", padx=20, pady=(0, 20))  
              
        #placeholder frame
        self.ph_frame = ctk.CTkFrame(
            self,
            fg_color="transparent",
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
            command=self.open_transfer_window
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
            command=self.change_pin_window
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
            command=self.statements_window
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
    

    def on_closing(self):
        """close login page in case of abrupt closing (The X in the window)"""
        if self.parent_login:
            self.parent_login.destroy()
        self.destroy()

    #center window function that can be used for any window (main or toplevel)
    def center_window(self, window=None):
        # if no window is provided, use "self" (the main window)
        win = window if window else self
    
        win.update_idletasks()
    
         # get dimensions of the specific window
        width = win.winfo_width()
        height = win.winfo_height()
    
        # get screen dimensions
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
    
        # calculate coordinates
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
    
        # Apply to the correct window
        win.geometry(f"{width}x{height}+{x}+{y}")


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
    
    def deposit_handling(self, dep_win):
        
        try:
            amount = float(dep_win.amount_entry.get())

            if amount <= 0:
                self.popup_win("Invalid Amount", "The amount must be greater than zero.")
                return

            success = models.Client.deposit(amount, self.current_client_id)

            if success == True:
                client_info = models.Admin.find_account(self.current_client_id)
                self.balance_label.configure(text=f"₪{client_info['balance']:,}")
                self.close_window(dep_win)
                self.popup_win("Deposit gone through!", f"Successfully deposited ₪{amount}")
            else:
                self.popup_win("Some thing gone wrrong!", "Please try again")

        except ValueError:
            self.popup_win("Invalid Amount", "The amount must be a number and greater than zero.")


    #open deposit window
    def open_window(self):
            dep_win = ctk.CTkToplevel(self)
            dep_win.title("Deposit")
            dep_win.geometry("400x400")
            dep_win.configure(fg_color="#0A0E27")
            dep_win.resizable(False, False)
            dep_win.grab_set() # prevents interaction with main dashboard until closed
            dep_win.attributes('-topmost', True)  # Keep on top
            
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
                command=lambda: self.deposit_handling(dep_win)
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

    def withdraw_logic(self, with_win):
        
        try:
            amount = float(with_win.amount_entry.get())
            if amount <= 0:
                print("invalid amount")
                self.popup_win("invalid amount", "amount must be greater than zero!")
                return

            success = models.Client.withdraw(amount, self.current_client_id)

            if success == True:
                client_info = models.Admin.find_account(self.current_client_id)
                self.balance_label.configure(text=f"₪{client_info['balance']:,}")
                self.close_window(with_win)
                self.popup_win("Success", f"Successfully withdraw ₪{amount}")
            else:
                self.popup_win("deposit failed.", "Please try again")

        except ValueError:
            print("Please enter a valid number")
            self.popup_win("Error", "Amount must be a number and greater than zero")

    #open withdraw window
    def open_withdraw_window(self):
            with_win = ctk.CTkToplevel(self)
            with_win.title("Withdraw")
            with_win.geometry("400x400")
            with_win.configure(fg_color="#0A0E27")
            with_win.resizable(False, False)
            with_win.attributes('-topmost', True)  # Keep on top
            
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
                command=lambda: self.withdraw_logic(with_win)
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


    def transfer_logic(self, trans_win):
        
        try:
            amount = float(trans_win.amount_entry.get())
            to_id = trans_win.recipient_entry.get()
            
            if amount <= 0:
                self.popup_win("invalid amount","Amount must be greater than zero!")
                return

            success = models.Client.transaction_fromto(amount, self.current_client_id, to_id)

            if success == True:
                client_info = models.Admin.find_account(self.current_client_id)
                self.balance_label.configure(text=f"₪{client_info['balance']:,}")
                self.close_window(trans_win)
                self.popup_win("Success", f"Successfully transferd ₪{amount} to {to_id}")
            else:
                self.popup_win("ERROR", "You either broke or the account you specified does not exist")

        except ValueError:
            self.popup_win("ERORR", "Please enter a number which is greater than zero")


    
    #open transfer window
    def open_transfer_window(self):
        trans_win = ctk.CTkToplevel(self)
        trans_win.title("Transfer Funds")
        trans_win.geometry("400x400")
        trans_win.configure(fg_color="#0A0E27")
        trans_win.resizable(False, False)
        trans_win.attributes('-topmost', True)
        
        #frame
        trans_win.frame = ctk.CTkFrame(
            trans_win, 
            corner_radius=20, 
            fg_color="#0A0E27")
        trans_win.frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        #label
        trans_win.with_label = ctk.CTkLabel(
            trans_win.frame,
            text="Transfer Funds",
            font=("Inter", 16, "bold"),
            text_color="white"
        )
        trans_win.with_label.pack(pady=20)
        
        #recipient ID entry
        trans_win.recipient_entry = ctk.CTkEntry(
            trans_win.frame,
            placeholder_text="Recipient ID",
            font=("Inter", 14),
            width=300,
            height=40,
            corner_radius=10,
            fg_color="#1F1F1F",
            text_color="white",
            border_width=0
        )
        trans_win.recipient_entry.pack(pady=10)
        
        #amount entry
        trans_win.amount_entry = ctk.CTkEntry(
            trans_win.frame,
            placeholder_text="Amount to transfer",
            font=("Inter", 14),
            width=300,
            height=40,
            corner_radius=10,
            fg_color="#1F1F1F",
            text_color="white",
            border_width=0
        )
        trans_win.amount_entry.pack(pady=10)
        
        #confirm button
        trans_win.confirm_btn = ctk.CTkButton(
            trans_win.frame,
            text="Confirm Transfer",
            width=300,
            height=40,
            corner_radius=10,
            fg_color="#3B82F6",
            hover_color="#2563EB",
            font=("Inter", 14, "bold"),
            command=lambda: self.transfer_logic(trans_win)
        )
        trans_win.confirm_btn.pack(pady=(30, 10))
        
        #cancel button
        trans_win.cancel_btn = ctk.CTkButton(
            trans_win.frame,
            text="Cancel",
            width=300,
            height=40,
            corner_radius=10,
            fg_color="#1F1F1F",
            hover_color="#3B3B3B",
            font=("Inter", 14, "bold"),
            command=lambda: self.close_window(trans_win)
        )
        trans_win.cancel_btn.pack(pady=0)
        self.center_window(trans_win)
    #logsout
    def logout(self):
        if self.parent_login:
            self.parent_login.deiconify() # show login window again
        self.destroy() # close dashboard window
    
    def change_pin_logic(self,change_pin_win):
        old_pin = change_pin_win.current_pin_entry.get()
        new_pin = change_pin_win.new_pin_entry.get()
        conf_pin = change_pin_win.confirm_new_pin_entry.get()

        if not old_pin or not new_pin or not conf_pin:
            self.popup_win("ERROR", "please fill in all pin fields.")
            return

        if new_pin != conf_pin:
            self.popup_win("ERROR", "New pin and Confirmation doesnt match.")
            return
        
        if new_pin == old_pin:
            self.popup_win("Invalid PIN", "New PIN cannot be the same as the old one.")
            return

        success = models.Client.change_pin(self.current_client_id, old_pin, new_pin)

        if success:
            self.popup_win("Success", f"PIN changed for client {self.current_client_id} ") 
            self.close_window(change_pin_win)
        else:
            self.popup_win("Error", "The PIN hasn't been changed, Please try again!")
    
    #open change pin window
    def change_pin_window(self):
        change_pin_win = ctk.CTkToplevel(self)
        change_pin_win.title("Change PIN")
        change_pin_win.geometry("400x500")
        change_pin_win.configure(fg_color="#0A0E27")
        change_pin_win.resizable(False, False)
        change_pin_win.attributes('-topmost', True)
        
        #frame
        change_pin_win.frame = ctk.CTkFrame(
            change_pin_win, 
            corner_radius=20, 
            fg_color="#0A0E27")
        change_pin_win.frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        #label
        change_pin_win.label = ctk.CTkLabel(
            change_pin_win.frame,
            text="Change PIN",
            font=("Inter", 16, "bold"),
            text_color="white"
        )
        change_pin_win.label.pack(pady=20)
        
        #current pin entry  
        change_pin_win.current_pin_entry = ctk.CTkEntry(
            change_pin_win.frame,
            placeholder_text="Current PIN",
            show="*", # hides input
            height=55,
            fg_color="#161C30",
            border_color="#90d5ff",
            text_color="white",
            corner_radius=12
        )
        change_pin_win.current_pin_entry.pack(fill="x", pady=10)
        
        #new pin entry
        change_pin_win.new_pin_entry = ctk.CTkEntry(
            change_pin_win.frame,
            placeholder_text="New PIN",
            show="*", # hides input
            height=55,
            fg_color="#161C30",
            border_color="#90d5ff",
            text_color="white",
            corner_radius=12
        )
        change_pin_win.new_pin_entry.pack(fill="x", pady=10)
        
        #confirm new pin entry
        change_pin_win.confirm_new_pin_entry = ctk.CTkEntry(
            change_pin_win.frame,
            placeholder_text="Confirm New PIN",
            show="*", # hides input
            height=55,
            fg_color="#161C30",
            border_color="#90d5ff",
            text_color="white",
            corner_radius=12
        )
        change_pin_win.confirm_new_pin_entry.pack(fill="x", pady=10)
        
        #confirm button
        change_pin_win.confirm_btn = ctk.CTkButton(
            change_pin_win.frame,
            text="Confirm PIN Change",
            width=300,
            height=40,
            corner_radius=10,
            fg_color="#3B82F6",
            hover_color="#2563EB",
            font=("Inter", 14, "bold"),
            command=lambda: self.change_pin_logic(change_pin_win)
        )
        change_pin_win.confirm_btn.pack(pady=(30, 10))
        
        #cancel button
        change_pin_win.cancel_btn = ctk.CTkButton(
            change_pin_win.frame,
            text="Cancel",
            width=300,
            height=40,
            corner_radius=10,
            fg_color="#1F1F1F",
            hover_color="#3B3B3B",
            font=("Inter", 14, "bold"),
            command=lambda: self.close_window(change_pin_win)
        )
        change_pin_win.cancel_btn.pack(pady=0)
        self.center_window(change_pin_win)
        
    #open statements window
    def statements_window(self):
        statements_win = ctk.CTkToplevel(self)
        statements_win.title("Statements")
        statements_win.geometry("800x500")
        statements_win.configure(fg_color="#0A0E27")
        statements_win.resizable(False, False)
        statements_win.attributes('-topmost', True)
        
        #! ////////////////////////////////////////////////////////////

        # this is the main transactios table
        main_frame = ctk.CTkFrame(statements_win, fg_color="transparent")
        main_frame.pack(expand=True, fill="both", padx=20, pady=(10, 20)) # pady=(Top, Bottom)
        
        # Title
        label = ctk.CTkLabel(
            main_frame,
            text="Transaction History",
            font=("Inter", 20, "bold"),
            text_color="white"
        )
        label.pack(pady=(0, 0))

        self.refresh_button = ctk.CTkButton(
            main_frame, 
            text="Refresh Table", 
            command=self.update_table, 
            fg_color="#3B82F6",
            hover_color="#2563EB"
        )
        # self.refresh_button.pack(pady=10, side="top")
        self.refresh_button.pack(pady=10)

        try:
            data = storage.all_clients()
            # Get user transactions
            user_data = data.get(str(self.current_client_id), {})
            transactions = user_data.get("transaction_list", [])
            
            # Define Table Headers
            table_values = [["Date", "Type", "Amount", "From/To", "Direction"]]
            
            for tx in reversed(transactions):
                date = tx.get("date", "N/A")
                tx_type = tx.get("type", "N/A").capitalize()
                amount = f"₪{abs(float(tx.get('amount', 0))):,.2f}"
                
                if tx.get("type") == "transfer":
                    other_party = tx.get("to") if tx.get("direction") == "out" else tx.get("from")
                    from_to = f"{other_party}"
                else:
                    from_to = "-"
                
                direction = tx.get("direction", "N/A").upper()
                
                table_values.append([date, tx_type, amount, from_to, direction])
            
            if len(table_values) == 1:
                table_values.append(["-", "No transactions found", "-", "-", "-"])

        except Exception as e:
            table_values = [["Error loading data"]]
            print(f"Error: {e}")

        scroll_frame = ctk.CTkScrollableFrame(
            main_frame, 
            fg_color="#161C30", 
            height=350
        )
        scroll_frame.pack(expand=True, fill="both", pady=10)

        # Initialize CTkTable with the retrieved data
        self.table = CTkTable(
            master=scroll_frame,
            row=len(table_values),
            column=5,
            values=table_values,
            header_color="#3B82F6",
            hover_color="#2563EB",
            colors=["#1F1F1F", "#2A2D3E"],
            text_color="white"
        )
        self.table.pack(expand=True, fill="both")
  
    def close_window(self, window):
        window.destroy()
        
    def update_table(self):
        try:
                data = storage.all_clients()
                # Get user transactions
                user_data = data.get(str(self.current_client_id), {})
                transactions = user_data.get("transaction_list", [])
                    
                # Define Table Headers
                table_values = [["Date", "Type", "Amount", "From/To", "Direction"]]
                    
                for tx in reversed(transactions):
                    date = tx.get("date", "N/A")
                    tx_type = tx.get("type", "N/A").capitalize()
                    amount = f"₪{abs(float(tx.get('amount', 0))):,.2f}"
                        
                    if tx.get("type") == "transfer":
                        other_party = tx.get("to") if tx.get("direction") == "out" else tx.get("from")
                        from_to = f"{other_party}"
                    else:
                        from_to = "-"
                        
                    direction = tx.get("direction", "N/A").upper()
                        
                    table_values.append([date, tx_type, amount, from_to, direction])
                    
                if len(table_values) == 1:
                    table_values.append(["-", "No transactions found", "-", "-", "-"])

        except Exception as e:
                table_values = [["Error loading data"]]
                print(f"Error: {e}")
        new_values = table_values
        self.table.configure(values=new_values)
        
if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()