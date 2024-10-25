# syncObsidian
An alternative using python, to sync your obsidian notes over devices.

If u are using powershell like me u can make this process even easier by editing ur custom commands

> notepad $PROFILE

function sync {
    python3 C:\dir\sync.py
}

function push {
    python3 C:\dir\push.py
}

CTRL + S
> . $PROFILE

ur commannds should now be updated, writing sync/push will call the scripts which makes the process a whole of a lot easier
