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

# Iterate through each line by index
for i in range(len(lines)):
    # Check if the line contains "error" (case-insensitive)
    if "error" in lines[i].lower():
        # Print the previous line if it exists
        if i - 1 >= 0:
            print(lines[i - 1])
        # Print the current line with "error"
        print(lines[i])
        # Print the next line if it exists
        if i + 1 < len(lines):
            print(lines[i + 1])
        # Print a blank line for separation
        print()

