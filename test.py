#!/usr/bin/env python3


import hid
import time




def pad_cmd(hex_list):
    # HID requires the first byte to be 0x00 (Report ID)
    packet = [0x00] + hex_list
    # Pad to 64 bytes if necessary (some devices require fixed-length)
    packet += [0x00] * (65 - len(packet))

    return packet


def send_cmd(device, packet):
    device.write(bytes(packet[:65]))



if __name__ == "__main__":
        
    VENDOR_ID = 0x28e9
    PRODUCT_ID = 0x028a

    EM_90 = hid.Device(vid=VENDOR_ID, pid=PRODUCT_ID)
    print("Connected")
    # This is a common "Start Data Transfer" command for these chipsets
    # [Report ID (0x00), Command Header, Command Type, ...Padding]
    # Note: The first byte must be 0x00 (the HID Report ID)
    cmd = [0x00, 0xAA, 0x17, 0x00, 0x00, 0x00, 0x00, 0x00] 
   
    print("Sending 'Import' command...")
    send_cmd(EM_90, pad_cmd(cmd))

    data = EM_90.read(64) # Read up to 64 bytes
    if data:
        # Print the raw hex so we can see the pattern
        print(f"ACK: {data.hex(' ')}")
    
    # Command: AA 15 (Common for "Get File List" or "Directory")
    send_cmd(EM_90, pad_cmd([0xAA, 0x15, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))


    data = EM_90.read(64) # Read up to 64 bytes
    if data:
        # Print the raw hex so we can see the pattern
        print(f"ACK: {data.hex(' ')}")
    
    print("Waiting for data (Ctrl+C to stop)...")
    while True:
        data = EM_90.read(64) # Read up to 64 bytes
        if data:
            # Print the raw hex so we can see the pattern
            print(f"Received: {data.hex(' ')}")
        else:
            time.sleep(0.1)
