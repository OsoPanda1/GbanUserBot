on_string = """
**Portable Psychological Diagnosis and Supression System**
Connection successful.
`Probe` is now active. 
Message scans are now possible!
"""

# Make sure not to change these too much
# If you still wanna change it change the regex too
scan_request_string = """
$SCAN
Message Scan request
**Enforcer:** {enforcer} 
**User scanned:** {spammer}
**Scan Reason:** `{reason}`
**Chat Originated from:** {chat}
**Target Message:** `{message}`
"""
forced_scan_string = """
$FORCED
**Inspector:** {ins}
**User scanned:** {spammer}
**Scan Reason:** `{reason}`
**Chat Originated from:** {chat}
**Target Message:** `{message}`
"""

reject_string = """
$REJECTED
**Crime Coefficient:** `Under 100`

Not a target for enforcement action. 
"""

proof_string = """
**Case file for** - {proof_id} :
┣━**Reason**: {reason}
┗━**Message**
         ┣━[Nekobin]({paste})
         ┗━[DelDog]({url})"""

scan_approved_string = """
#BANNED
**Target User:** {scam}
**Reason:** `{reason}`
**Enforcer:** `{enforcer}`
**Case Number:** `{proof_id}`
"""

bot_gban_string = """
#DestroyDecomposer
**Enforcer:** `{enforcer}`
**Target User:** {scam}
**Reason:** `{reason}`
"""

# https://psychopass.fandom.com/wiki/Crime_Coefficient_(Index)
# https://psychopass.fandom.com/wiki/The_Dominator
