#!/usr/bin/env python3

import hid

def list_devices():
    print(f"{'Manufacturer':<20} | {'Product':<25} | {'VID:PID'}")
    print("-" * 65)
    for device in hid.enumerate():
        # Formatting to 4-digit hex for easy copy-pasting
        vid = f"{device['vendor_id']:04x}"
        pid = f"{device['product_id']:04x}"
        mfg = device['manufacturer_string'] or "Unknown"
        prod = device['product_string'] or "Unknown"
        
        print(f"{mfg:<20} | {prod:<25} | {vid}:{pid}")

if __name__ == "__main__":
    list_devices()
