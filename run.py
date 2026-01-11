import importlib
import requests
import uuid
import hashlib
import platform
import os
import sys
import re
import pystyle
import random
import subprocess
from time import sleep

R = "\033[31m"
G = "\033[32m"
Y = "\033[33m"
B = "\033[34m"
P = "\033[35m"
C = "\033[36m"
W = "\033[0m"
# ================= LOGO =================
def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{G}
              ██   ███████   ███    ███ 
              ██   ██   ██   ████  ████ 
              ██   ███████   ██ ████ ██ 
         ██   ██   ██   ██   ██  ██  ██ 
         ███████   ██   ██   ██      ██  
AUTO CREATE PAGE WITH DP UPLOAD TOKEN BASED SOFTWARE {W}""")

def Privacy():
    # 🔑 Keep this private!
    secret_salt = "JAM-SHAHRUKH-LAAR-PERSONAL-KEY"

    # ✅ Use system info for stable ID (no file, no MAC)
    sys_info = f"{platform.system()}|{platform.release()}|{platform.version()}|{platform.machine()}|{platform.node()}"

    # Combine with salt
    raw_key = sys_info + secret_salt

    # Generate SHA256 hash
    hash_key = hashlib.sha256(raw_key.encode()).hexdigest().upper()

    # Format like XXXX-XXXX-XXXX-XXXX-XXXX
    formatted_key = '-'.join(hash_key[i:i+4] for i in range(0, 20, 4))
    keymay = formatted_key + '|Tools'

    # ✅ Use proper Google Docs export link
    url = "https://docs.google.com/document/d/1owduWvAeSJnSZKTPHmfx0JT6qqUvZeN7vafC3ymtCb0/edit?tab=t.0"
    try:
        k = requests.get(url, timeout=10).text
    except Exception as e:
        print(f"\033[0;31m[ERROR]\033[0m Could not fetch Google Doc: {e}")
        sleep(5)
        quit()

    # === Security check ===
    if keymay in k:
        print("                   \033[0;92m|\033[7mACCESS APPROVED\033[0m\033[1;92m|")
    else:
        print(f"\n                \033[0;31m|\033[7mACCESS NOT APPROVED\033[0m\033[1;91m|")
        print(f"\n  System Key: \033[1;93m{keymay}\033[0m\n")
        sleep(20)
        quit()

    print(f"{G}ACCESS APPROVED{W}")
MENU = {
    1: ("tool1", "main", "GET-TOKEN (cookie based)"),
    2: ("tool", "main_menu", "COMMENT-RC + VOTING (cookie + token based)"),
    3: ("tool2", "main_jam", "POLL-VOTING (token based)"),
    4: ("tool3", "main", "POST/COMMENT/VIDEO-REACTION (cookie based)"),
    5: ("tool4", "main", "PAGE-CREATE-WITH-DP (token based)"),
    6: ("tool5", "main", "FOLLOWER (token based)"),
    7: ("tool6", "main", "PAGE-ACTIVATE (cookie based)"),
    8: ("tool7", "main_dismiss", "SET-DISMISS-ACCOUNTS (cookie based)"),
    9: ("tool8", "main", "UPLOAD-PAGES-DPZ (token based)"),
    10: ("tool9", "main_live", "CHECK-LIVE-COOKIE"),
    11: ("tool10", "main", "CHECK-LIVE-TOKEN-WITH-SHOW-TOTAL-PAGES"),
}

def main():
    logo()
    Privacy()
    print("\n======= TOOL MENU =======\n")

    for num, (_, _, name) in MENU.items():
        print(f"[{num}] {name}")

    try:
        choice = int(input("\nSelect option (1–11): ").strip())
    except ValueError:
        print("❌ Please enter a number")
        sys.exit(1)

    if choice not in MENU:
        print("❌ Invalid selection")
        sys.exit(1)

    module_name, func_name, _ = MENU[choice]

    try:
        module = importlib.import_module(module_name)
        getattr(module, func_name)()
    except Exception as e:
        print(f"❌ Failed to run {module_name}")
        print(e)

if __name__ == "__main__":
    main()
