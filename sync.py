import os
import subprocess
import urllib.parse
import json

def exec(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Couldn't execute {command}")
        print(f"Error: {result.stderr.strip()}") 
        return None 
    return result.stdout

def sync(repo_url, target_dir):
    if not os.path.exists(target_dir):
        print(f"Cloning repo {repo_url} into {target_dir}")
        if exec(f"git clone {repo_url} {target_dir}") is None:
            return
    else:
        print(f"Pulling latest changes in {target_dir}")
        if not os.path.exists(os.path.join(target_dir, '.git')):
            print(f"The directory {target_dir} is not a git repository.")
            return
        current_dir = os.getcwd()
        os.chdir(target_dir)
        exec("git pull")
        os.chdir(current_dir)

def push_changes(repo_url, target_dir, commit_message="Update"):
    if not os.path.exists(target_dir):
        print(f"The directory {target_dir} does not exist.")
        return
    
    if not os.path.exists(os.path.join(target_dir, '.git')):
        print(f"The directory {target_dir} is not a git repository.")
        return
    
    current_dir = os.getcwd()
    os.chdir(target_dir)

    if exec(f"git remote set-url origin {repo_url}") is None:
        os.chdir(current_dir)
        return
    
    exec("git add .")

    commit_out = exec(f'git commit -m "{commit_message}"')
    if commit_out is None:
        if "nothing to commit" in exec("git status"):
            print("No changes to commit.")
        os.chdir(current_dir)
        return

    exec("git push")
    print(f"Changes have been committed with message: {commit_message}")

    os.chdir(current_dir)

def load_config(config_path='config.json'):
    if not os.path.isfile(config_path):
        print(f"Error: Configuration file '{config_path}' not found.")
        exit(1)
    
    with open(config_path, 'r') as file:
        config = json.load(file)
    
    # URL encode the token to handle special characters
    config['token'] = urllib.parse.quote(config['token'], safe='')

    # Build the full repo URL for each repository
    for repo in config['repos']:
        repo_url = f"https://{config['username']}:{config['token']}@github.com/{config['username']}/{repo['repo_name']}.git"
        repo['url'] = repo_url
        repo['target_dir'] = os.path.join(config['vault_dir'], repo['name'])
    
    return config

def main():
    config = load_config()

    for repo in config['repos']:
        print(f"Repository: {repo['name']} located at {repo['target_dir']}")
        action = input("Do you want to (S)ync or (P)ush changes? ").strip().lower()

        if action == 's':
            sync(repo['url'], repo['target_dir'])
        elif action == 'p':
            commit_message = input("Enter the commit message: ")
            push_changes(repo['url'], repo['target_dir'], commit_message)
        else:
            print("Invalid action. Please choose 'S' for sync or 'P' for push.")

if __name__ == "__main__":
    main()
