'''Print All Plug/Unplug USB Events
Description: Print all lines that indicate a USB device was plugged in or 
unplugged (look for "USB disconnect" or "new full-speed USB device" in the log lines).
Sample Input:log = """
[22.1] usb 1-1: USB disconnect, device number 2
[22.3] usb 1-1: new full-speed USB device number 3 using xhci_hcd
[22.5] usb 2-1: reset high-speed USB device number 4 using ehci-pci"""
Expected Output:[22.1] usb 1-1: USB disconnect, device number 2
[22.3] usb 1-1: new full-speed USB device number 3 using xhci_hcd'''


log = """
[22.1] usb 1-1: USB disconnect, device number 2
[22.3] usb 1-1: new full-speed USB device number 3 using xhci_hcd
[22.5] usb 2-1: reset high-speed USB device number 4 using ehci-pci
"""
patterns = ["usb disconnect", "new full-speed usb device"]

# Split the log into lines
lines = log.strip().splitlines()

for line in lines:
    line_lower = line.lower()
    if any(p in line_lower for p in patterns):
        print(line)
