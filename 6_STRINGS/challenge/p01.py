'''Count Number of Kernel Panics and Oops
Description: Given a string containing kernel logs, count how many times "kernel panic" and "Oops" appear (case-insensitive).
sample input:log = """[12345.67] kernel panic - not syncing: Fatal exception
[12345.89] Oops: 0002 [#1] SMP
[12346.00] kernel panic - not syncing: Fatal exception
[12346.13] Oops: 0003 [#2] SMP"""
Expected Output:
Kernel panic count: 2
Oops count: 2'''

log = """
[12345.67] kernel panic - not syncing: Fatal exception
[12345.89] Oops: 0002 [#1] SMP
[12346.00] kernel panic - not syncing: Fatal exception
[12346.13] Oops: 0003 [#2] SMP
"""

# Convert log to lowercase for case-insensitive match
log_lower = log.lower()

# Count occurrences
panic_count = log_lower.count("kernel panic")
oops_count = log_lower.count("oops")

# Output result
print("Kernel panic count:", panic_count)
print("Oops count:", oops_count)
