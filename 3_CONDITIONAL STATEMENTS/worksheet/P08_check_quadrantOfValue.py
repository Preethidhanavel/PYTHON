'''Given a digital input value (0–255), determine and print which of 4 quadrants it falls into:
- 0–63, 64–127, 128–191, 192–255'''
# Take input from user for a digital value between 0 and 255
v = int(input("Enter the digital value between 0-255: "))

# Check which quadrant (range) the value falls into
if v >= 0 and v <= 63:
    print(f"{v} falls in quadrant 0-63")      # First quadrant
elif v >= 64 and v <= 127:
    print(f"{v} falls in quadrant 64-127")    # Second quadrant
elif v >= 128 and v <= 191:
    print(f"{v} falls in quadrant 128-191")   # Third quadrant
elif v >= 192 and v <= 255:
    print(f"{v} falls in quadrant 192-255")   # Fourth quadrant
