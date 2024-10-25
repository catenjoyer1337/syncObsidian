import json
import os
import subprocess
import urllib.parse
from dotenv import load_dotenv

def exec(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Couldn't execute {command}")
        print(f"Error: {result.stderr.strip()}")
        return None
    return result.stdout

def load_config(config_path='config.json'):
    load_dotenv()

    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, config_path)

    if not os.path.isfile(config_path):
        print(f"Error: Configuration file '{config_path}' not found.")
        exit(1)

    with open(config_path, 'r') as file:
        config = json.load(file)

    config['username'] = os.getenv("GITHUB_NAME")
    config['token'] = urllib.parse.quote(os.getenv("GITHUB_TOKEN", ""), safe='')
    config['vault_dir'] = os.getenv("VAULT_DIR")

    for repo in config['repos']:
        repo_url = f"https://{config['username']}:{config['token']}@github.com/{config['username']}/{repo['repo_name']}.git"
        repo['url'] = repo_url
        repo['target_dir'] = os.path.join(config['vault_dir'], repo['name'])

    return config

def ensure_safe_directory(repo_dir):
    command = f'git config --global --add safe.directory "{repo_dir}"'
    exec(command)

def is_repo_synced(repo_dir):
    ensure_safe_directory(repo_dir)
    current_dir = os.getcwd()
    os.chdir(repo_dir)

    status_output = exec("git status")
    os.chdir(current_dir)

    if status_output is None:
        print(f"Failed to check status for {repo_dir}.")
        with open("error_log.txt", "a") as log_file:
            log_file.write(f"Git status failed for {repo_dir}\n")
        return False

    if "nothing to commit" in status_output:
        return True

    return False
