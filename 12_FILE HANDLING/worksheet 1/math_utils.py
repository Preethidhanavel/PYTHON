
import re

def process_log_file(filename):
    with open(filename, 'r') as file:
        return file.readlines()

def extract_severity(line):
    match = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3} (?P<level>[A-Z]+):", line)
    if match:
        return match.group("level")
    return None