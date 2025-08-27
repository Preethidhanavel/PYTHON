'''Top 3 Most Frequent Error Keywords
Description: Given a kernel log string, count the most frequent 
error keywords: "fail", "error", "timeout", "panic" (case-insensitive). Show the top 3 with their counts.
sample input:log = """
[1.11] ERROR: device failed to start
[1.12] ERROR: timeout waiting for response
[1.13] WARNING: low battery
[1.14] PANIC: unrecoverable error
[1.15] device fail detected
[1.16] timeout on bus"""
Expected Output:
error: 3
fail: 2
timeout: 2
'''
from collections import Counter

log = """
[1.11] ERROR: device failed to start
[1.12] ERROR: timeout waiting for response
[1.13] WARNING: low battery
[1.14] PANIC: unrecoverable error
[1.15] device fail detected
[1.16] timeout on bus
"""

keywords = ["fail", "error", "timeout", "panic"]

log_lower = log.lower()

# Count keyword occurrences
counts = Counter()

for keyword in keywords:
    counts[keyword] = log_lower.count(keyword)

# Get top 3 most frequent keywords
top3 = counts.most_common(3)

# Print result
for word, count in top3:
    print(f"{word}: {count}")
