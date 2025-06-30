''' Command-Line Tool
 Covers: Command-line argument parsing and list comprehensions
 Description: Create a script that accepts file names and search terms from the command line, 
processes logs, and outputs filtered results.'''

import os
import glob
import re
from collections import defaultdict

LOG_PATTERN = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3} (?P<level>[A-Z]+):"

def extract_severity(line):
    match = re.search(LOG_PATTERN, line)
    return match.group("level") if match else None

def process_log_file(filepath):
    counts = defaultdict(int)
    with open(filepath, 'r') as file:
        for line in file:
            level = extract_severity(line)
            if level:
                counts[level] += 1
    return counts

def aggregate_logs_from_directory(directory):
    summary = defaultdict(int)
    log_files = glob.glob(os.path.join(directory, "*.log"))
    
    if not log_files:
        print("No .log files found in the directory.")
        return summary

    for log_file in log_files:
        file_counts = process_log_file(log_file)
        print(f"{log_file} ", dict(file_counts)) 
        for level, count in file_counts.items():
            summary[level] += count

    return summary


directory = input("Enter directory path containing .log files: ").strip()
    
if not os.path.isdir(directory):
    print(f"Directory '{directory}' not found.")
    exit()

summary = aggregate_logs_from_directory(directory)

print("\nLog Level Summary:")
for level, count in summary.items():
    print(f"{level}: {count}")


