'''Highlight All Error Lines and Show Context
Description: For each line containing "error" (case-insensitive), print that line plus the previous and next line for context.
Sample Input:log = """
[10.00] Starting system
[10.05] Initializing drivers
[10.10] ERROR: Device not found
[10.15] Trying next device
[10.20] ERROR: Timeout waiting for response
[10.25] Reboot recommended"""
Expected Output:
[10.05] Initializing drivers
[10.10] ERROR: Device not found
[10.15] Trying next device

[10.15] Trying next device
[10.20] ERROR: Timeout waiting for response
[10.25] Reboot recommended'''


log = """
[10.00] Starting system
[10.05] Initializing drivers
[10.10] ERROR: Device not found
[10.15] Trying next device
[10.20] ERROR: Timeout waiting for response
[10.25] Reboot recommended
"""

# Split log into individual lines
lines = log.strip().splitlines()

for i in range(len(lines)):
    if "error" in lines[i].lower():
        if i - 1 >= 0:
            print(lines[i - 1])
        print(lines[i])
        if i + 1 < len(lines):
            print(lines[i + 1])
        print()  
