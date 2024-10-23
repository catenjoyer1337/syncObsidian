# syncObsidian 🟣

A Python-based alternative to easily sync your Obsidian notes across multiple devices.

If you're like me and use PowerShell, you can streamline this process even further by customizing your commands. Here's how:

### PowerShell Custom Commands

Open your profile in Notepad to set up some handy functions:

```powershell
notepad $PROFILE
```

Then, add the following to your profile:

```powershell
# OBSIDIAN
# List contents of your Obsidian vault
function lsob { Get-ChildItem "C:\Documents\Vault" }

# Sync Obsidian notes
function sync {
    Set-Location "C:\syncObsidian"
    python .\sync.py
}
```

Save the file (`CTRL + S`), then update your session with:

```powershell
. $PROFILE
``

### 🚀 Usage

- **`lsob`** — Lists all items in your Obsidian vault directory.
- **`sync`** — Runs the Python sync script to keep your notes updated.

Happy note-syncing! 📝✨

---
