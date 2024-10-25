from main_menu import display_main_screen, wait_for_user_input, clear_screen
from utils import load_config, exec, is_repo_synced
import os
import json
import git

def check_repos():
    config = load_config()

    print("\nChecking repos...")
    repos_to_sync_or_clone = []

    for i, repo in enumerate(config['repos'], start=1):
        repo_name = repo['name']
        target_dir = repo['target_dir']
        
        if os.path.exists(target_dir):
            synced = is_repo_synced(target_dir)
            status = 'Synced' if synced else 'Unsynced'
            print(f"{i}. {repo_name} - {status}")
            if not synced:
                repos_to_sync_or_clone.append(repo)
        else:
            print(f"{i}. {repo_name} - Not Cloned")
            repos_to_sync_or_clone.append(repo)

    if repos_to_sync_or_clone:
        action = input("\nWould you like to clone/sync these repositories? (1/Y - Clone/Sync, 2/N - Leave alone): ").strip().lower()
        if action in ['1', 'y', 'Y']:
            for repo in repos_to_sync_or_clone:
                clone_or_sync_repo(repo)
        else:
            print("Leaving repositories alone.")

def clone_or_sync_repo(repo):
    target_dir = repo['target_dir']
    if os.path.exists(target_dir):
        print(f"Synchronizing {repo['name']}...")
        os.chdir(target_dir)
        os.system("git pull")
        print(f"Successfully synchronized {repo['name']}.")
    else:
        print(f"Cloning {repo['name']}...")
        add_repo(repo['repo_name'])

def prompt_user_for_action(actions_needed):
    if actions_needed:
        user_action = input("\nWould you like to take action on these repositories? (1/Y - Clone/Sync, 2/N - Leave alone): ").strip().lower()

        if user_action in ['1', 'y']:
            for repo in actions_needed:
                print(f"Cloning/Synchronizing {repo['name']}...")
        else:
            print("Leaving repositories alone.")
    else:
        print("All repositories are synced or cloned.")

def search_repo():
    config = load_config()
    search_term = input("Enter repo name to search: ").strip()
    found_repo = next((repo for repo in config['repos'] if repo['repo_name'] == search_term), None)

    if found_repo:
        print(f"Repo '{found_repo['repo_name']}' found!")
        synced = is_repo_synced(found_repo['target_dir'])
        print(f"Status: {'Synced' if synced else 'Unsynced'}")
    else:
        print(f"Repo '{search_term}' not found in config.")

def add_repo(repo_name):
    config = load_config()
    
    username = config["username"]
    token = config["token"]
    vault_dir = config["vault_dir"]
    
    repo_url = f"https://{username}:{token}@github.com/{username}/{repo_name}.git"
    target_dir = os.path.join(vault_dir, repo_name)

    if os.path.exists(target_dir):
        print(f"Repo '{repo_name}' already exists at '{target_dir}'.")
        return

    try:
        git.Repo.clone_from(repo_url, target_dir)
        print(f"Successfully cloned repo '{repo_name}' to '{target_dir}'.")

        new_repo = {
            "name": repo_name, 
            "repo_name": repo_name,
            "url": repo_url,
            "target_dir": target_dir
        }
        config['repos'].append(new_repo)

        current_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(current_dir, 'config.json')
        
        with open(config_path, 'w') as file:
            json.dump(config, file, indent=4)

        print(f"Added repo '{repo_name}' to config.")
    
    except Exception as e:
        print(f"Failed to clone repo '{repo_name}': {e}")



def remove_repo():
    config = load_config()
    repo_name = input("Enter the repo name to remove: ").strip()

    repo_to_remove = next((repo for repo in config['repos'] if repo['repo_name'] == repo_name), None)

    if repo_to_remove:
        target_dir = repo_to_remove['target_dir']
        
        if os.path.exists(target_dir):
            try:
                import shutil
                shutil.rmtree(target_dir)
                print(f"Successfully deleted '{target_dir}'.")
            except Exception as e:
                print(f"Failed to delete '{target_dir}': {e}")
        else:
            print(f"Directory '{target_dir}' does not exist. Skipping deletion.")
        
        config['repos'] = [repo for repo in config['repos'] if repo['repo_name'] != repo_name]

        current_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(current_dir, 'config.json')
        
        with open(config_path, 'w') as file:
            json.dump(config, file, indent=4)

        print(f"Removed repo '{repo_name}' from config.")
    else:
        print(f"Repo '{repo_name}' not found in config.")

def main():
    while True:
        display_main_screen()
        user_input = wait_for_user_input()
        clear_screen()

        if user_input == "1":
            check_repos()
        elif user_input == "2":
            search_repo()
        elif user_input == "3":
            repo_name = input("Enter the repository name to add: ").strip()
            add_repo(repo_name)
        elif user_input == "4":
            remove_repo()
        elif user_input in ["0", "exit", "Q", "q", "quit", ":q"]:
            exit()
        else:
            print("Invalid command!")
        
        input("\nPress Enter to return to the main menu...")


if __name__ == "__main__":
    main()
