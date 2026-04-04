
from PIL import Image, ImageTk
import customtkinter as ctk
from CTkTable import *
import sys
import os
#?--> use the command if you dont have CTkTable > pip install CTkTable

from ui_windows import ui_dashboard
from ui_windows import ui_admin_login

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

import models
import storage
import json
MAIN_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(MAIN_DIR, "data.json")