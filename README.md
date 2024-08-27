
# syncObsidian
An alternative using python, to sync your obsidian notes over devices.

If u are using powershell like me u can make this process even easier by editing ur custom commands

> notepad $PROFILE
```
# OBSIDIAN
# list contents of vault
function lsob { gci "C:\Documents\Vault" }

function sync {
    Set-Location "C:\syncObsidian"
    python .\sync.py
}
```

CTRL + S
> . $PROFILE

lsob -> list items in vault directory<br/>
sync -> starts the script
