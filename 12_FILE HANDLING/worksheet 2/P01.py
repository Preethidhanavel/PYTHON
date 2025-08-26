'''Log Level Counter
 Write a script that reads the provided log file and counts the number of occurrences of each 
log level (INFO, DEBUG, WARNING, ERROR) using file I/O and dictionaries. Avoid using 
regular expressions for this task.
 Challenge: Ensure your code gracefully handles lines that do not follow the expected 
format.'''

from collections import defaultdict

def count_log_levels(filename):
    counts = defaultdict(int)
    expected_levels = {"INFO", "DEBUG", "WARNING", "ERROR"}

    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) >= 3:
                    level_with_colon = parts[2]  
                    if level_with_colon.endswith(":"):
                        level = level_with_colon[:-1] 
                        if level in expected_levels:
                            counts[level] += 1
                        else:
                            print(f"Ignored unknown level: {level_with_colon} in line: {line.strip()}")
                    else:
                        print(f"Ignored line without colon after level: {line.strip()}")
                else:
                    print(f"Ignored malformed line: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

    return counts

log_file = input("Enter log file name: ").strip()
level_counts = count_log_levels(log_file)

print("\nLog Level Summary:")
for level, count in level_counts.items():
    print(f"{level}: {count}")
