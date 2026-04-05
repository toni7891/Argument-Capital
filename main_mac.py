import sys
import os

#! this is the main file in the project for MacOS.

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from ui_windows import test_final_ui
from ui_windows import test_ui_mac

def main():
    app_login_screen = test_ui_mac.LoginScreen()
    app_login_screen.mainloop()

if __name__ == "__main__":
    main()
