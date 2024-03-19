import time
import board
import busio
from adafruit_pn532.uart import PN532_UART

# UART connection
uart = busio.UART(board.GP4, board.GP5, baudrate=115200, timeout=1)
pn532 = PN532_UART(uart, debug=False)

ic, ver, rev, support = pn532.firmware_version
print("Found PN532 with firmware version: {0}.{1}".format(ver, rev))

# Configure PN532 to communicate with MiFare cards
pn532.SAM_configuration()

print("Waiting for RFID/NFC card...")
while True:
    # Check if a card is available to read
    uid = pn532.read_passive_target(timeout=0.1)  # Check for a card every 0.5 seconds
    if uid is not None:
        print("Found card with UID:", [hex(i) for i in uid])
    else:
        print("No card detected.")
    time.sleep(0.1)