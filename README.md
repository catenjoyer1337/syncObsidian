# syncObsidian

syncObsidian is a CLI tool designed for syncing GitHub repositories to local directories in your Obsidian vault. Ideal for users who frequently work across multiple devices, it automates the syncing of repositories, making it easy to keep notes, code, or any files in sync across systems. With options for cloning, syncing, adding, and removing repositories, syncObsidian ensures a seamless setup for collaborative or personal workflows.

![CLI Preview](https://i.imgur.com/oDB1IJD.png)

## Features
- **Automatic Syncing**: Syncs local folders in your vault with GitHub repositories.
- **Repository Management**: Add and remove repositories from your sync list.
- **Minimal Configuration**: Uses a `config.json` file and environment variables for easy setup.
- **Error Handling**: Handles permissions and ownership issues for smooth syncing across different machines.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/syncObsidian.git
   cd syncObsidian
   ```

2. **Install dependencies**:
   This tool requires the GitPython library. Install it with:
   ```bash
   pip install gitpython
   ```

3. **Configure your environment**:
   Create a `.env` file in the project root with your GitHub username and token:
   - `GITHUB_USERNAME`: Your GitHub username (used for API requests).
   - `GITHUB_TOKEN`: A [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) with repo access for private repositories.
   - `VAULT_DIR`: The local directory/vault where repositories will be synced/stored.

4. **Set up `config.json`:**
   - Open the `config.json` file and adjust the placeholders as needed.

## Usage

- **Clone/Sync Repositories**
   syncObsidian will check for unsynced or untracked repositories and prompt you to clone or sync as needed.

- **Add a New Repository**
   Enter the repository name when prompted, and syncObsidian will handle the rest.

- **Remove a Repository**
   Enter the repository name to remove it from the configuration and delete its local directory.

## Troubleshooting

If you encounter an error related to "dubious ownership," ensure that the repository’s directory permissions match the user running the script. For more details, see the error message output and the [Git configuration documentation](https://git-scm.com/docs/git-config).
