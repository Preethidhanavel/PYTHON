'''Extract All Lines Containing WARNING With Timestamps
Description: From a multiline log string, print all lines that include the word "WARNING" (case-insensitive), 
including their timestamps.
sample input:log = """
[100.123] INFO: Booting Linux
[100.456] WARNING: Low memory detected
[101.000] WARNING: CPU load high
[101.555] INFO: Boot complete
"""
Expected Output:
[100.456] WARNING: Low memory detected
[101.000] WARNING: CPU load high'''
log = """
[100.123] INFO: Booting Linux
[100.456] WARNING: Low memory detected
[101.000] WARNING: CPU load high
[101.555] INFO: Boot complete
"""

# Split the log into individual lines
lines = log.strip().splitlines()

# Loop and filter lines with 'WARNING' (case-insensitive)
for line in lines:
    if "warning" in line.lower():
        print(line)
