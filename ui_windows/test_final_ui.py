import customtkinter as ctk
import os
import sys
from PIL import Image, ImageTk

# no idea found fix in youtube video python simplified
current_dir = os.path.dirname(os.path.abspath(__file__)) 
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

import models
from ui_windows import ui_dashboard
from ui_windows import ui_admin_login
import storage
import json

# FYI fitussi - hours for this
# https://github.com/TomSchimansky/CustomTkinter/discussions/2214
#↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#* added try except for using mac

#! THIS IS THE WORKING VERSION FOR WINDOWS! 


try:
    import pywinstyles
    USE_STYLES = True
except ImportError:
    USE_STYLES = False
    print("Running on non-Windows system: pywinstyles disabled")


class LoginScreen(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Argument Capital Login")
        self.geometry("400x700")
        self.resizable(False, False)
        self.configure(fg_color="#0A0E27")
        self.canvas = ctk.CTkCanvas(self, width=400, height=700, highlightthickness=0, bd=0)
        self.canvas.pack(fill="both", expand=True)

        bg_image_raw = Image.open("ArguCapiLogo.jpg")
        bg_image_resized = bg_image_raw.resize((400, 700))
        self.tk_bg_image = ImageTk.PhotoImage(bg_image_resized)
        self.canvas.create_image(0, 0, image=self.tk_bg_image, anchor="nw")
        self.canvas.image = self.tk_bg_image 


        self.username_entry = ctk.CTkEntry(
            self,
            placeholder_text="A c c o u n t    I D",
            placeholder_text_color="#000000",
            height=55,
            width=300,
            border_color="#121212",
            text_color="black",
            fg_color="transparent",
            bg_color="#000001",
            corner_radius=12,
            font=("Arial", 18, "bold"),
            border_width=3,
            justify="center"
        )
        if USE_STYLES:
            pywinstyles.set_opacity(self.username_entry, color="#000001")
        self.canvas.create_window(200, 350, window=self.username_entry, anchor="center")

        self.password_entry = ctk.CTkEntry(
            self,
            placeholder_text="P I N",
            show="*",
            placeholder_text_color="#000000",
            text_color="black",
            fg_color="#000001", 
            bg_color="#000001",
            font=("Arial", 18, "bold"), 
            border_color="#121212",
            height=55,
            width=300,
            corner_radius=12,
            border_width=3,
            justify="center"
        )
        if USE_STYLES:
            pywinstyles.set_opacity(self.password_entry, color="#000001")
        self.canvas.create_window(200, 420, window=self.password_entry)

        self.login_btn = ctk.CTkButton(
            self,
            text="Log In",
            height=55,
            width=300,
            fg_color="#3B82F6",
            hover_color="#2563EB",
            bg_color="#000001",
            font=("Inter", 16, "bold"),
            corner_radius=12,
            command=self.authenticate_and_open
        )
        if USE_STYLES:
            pywinstyles.set_opacity(self.login_btn, color="#000001")
        self.canvas.create_window(200, 520, window=self.login_btn)

        self.admin_btn = ctk.CTkButton(
            self,
            text="🛡️ A d m i n  L o g i n",
            fg_color="transparent",
            text_color="#000000",
            bg_color="#000001",
            font=("Arial", 18, "bold"), 
            border_color="#121212",
            border_width=3,
            height=55,
            width=300,
            corner_radius=12,
            command=self.open_admin_login
        )
        if USE_STYLES:
            pywinstyles.set_opacity(self.admin_btn, color="#000001")
        self.canvas.create_window(200, 650, window=self.admin_btn)
        self.center_window()


    def center_window(self, window=None):
        """_this function puts the window we are launching in the middle of the screen, relative to the dimensions of it._

        Args:
            window (_type_, object): _description_. Defaults to None.
        """
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
    
        # apply to the correct window
        win.geometry(f"{width}x{height}+{x}+{y}")


    def popup_win(self,title, message):
            popup_win = ctk.CTkToplevel(self)
            popup_win.title(title)
            popup_win.geometry("300x150")
            popup_win.configure(fg_color="#0A0E27")
            popup_win.resizable(False, False)
            popup_win.attributes("-topmost", True)
            popup_win.grab_set(),


            popup_label = ctk.CTkLabel(popup_win, text=message, font=("Inter", 13), wraplength=250, text_color="white",)
            popup_label.pack(pady=20)

            ok_btn = ctk.CTkButton(
                popup_win,
                text="OK", 
                width=100, 
                command=popup_win.destroy,
                fg_color="#3B82F6"
            )
            ok_btn.pack(pady=10)
        
            self.center_window(popup_win)

    def authenticate_and_open(self):
        """_this function is the basic "authentication" logic we are using in the client (normal user) interface._
        """
        client_id = self.username_entry.get()
        pin = self.password_entry.get()

        success = models.Client.check_pin(client_id, pin)
        
        if success == True:
            
            self.withdraw() 
        
            dashboard = ui_dashboard.Dashboard(current_client_id=client_id, parent_login=self)
            dashboard.mainloop()

        elif success == 2:
            self.popup_win("Failed to authenticate", "Account is BLOCKED! contact an admin!")
        else:
            self.popup_win("Failed to authenticate", "one or more of the credentials is incorrect")

    def open_admin_login(self):
        #if we get here it's because the user chose the admin login screen.
        self.destroy()
        admin_login = ui_admin_login.AdminLoginScreen()
        admin_login.mainloop()

if __name__ == "__main__":
    #FYI fittusi idk whats that doing but this works and fixed bullerd text -> https://stackoverflow.com/questions/41315873/attempting-to-resolve-blurred-tkinter-text-scaling-on-windows-10-high-dpi-disp
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass
        
    app = LoginScreen()
    app.mainloop()