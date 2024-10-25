import os
from shutil import get_terminal_size

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_main_screen():
    clear_screen()

    banner = '''
       _         _     _ _             
      | |       (_)   | (_)            
  ___ | |__  ___ _  __| |_  __ _ _ __  
 / _ \\| '_ \\/ __| |/ _` | |/ _` | '_ \\ 
| (_) | |_) \\__ \\ | (_| | | (_| | | | |
 \\___/|_.__/|___/_|\\__,_|_|\\__,_|_| |_| 
         ___ _   _ _ __   ___          
        / __| | | | '_ \\ / __|         
        \\__ \\ |_| | | | | (__          
        |___/\\__, |_| |_|\\___|         
              __/ |                    
             |___/                     
'''
    width = get_terminal_size().columns
    centered_banner = '\n'.join([line.center(width) for line in banner.splitlines()])
    
    print(centered_banner)
    print("-" * width)

    print("1. Check Repos")
    print("2. Search Repo")
    print("3. Add Repo")
    print("4. Remove Repo")
    print("-" * width)

def wait_for_user_input():
    """Waits for user input."""
    return input("\n> ").strip()


