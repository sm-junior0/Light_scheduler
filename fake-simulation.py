# fake-simulation.py
import utils.transport
import utils.session
import serial
import serial.threaded
import time

class FakeArduino(serial.threaded.Protocol):
    def __init__(self):
        super().__init__()

    def data_received(self, data):
        message = data.decode('utf-8').strip()
        print(f"💬 Fake Arduino received: {message}")

        if message == "ON":
            print("🔴 Relay simulated ON")
        elif message == "OFF":
            print("🔵 Relay simulated OFF")
        else:
            print("❓ Unknown command received")

def main():
    print("🛠 Starting Fake Arduino COM5 emulator...")
    
    # Open virtual serial port
    ser = serial.serial_for_url('loop://', baudrate=9600, timeout=1)
    protocol = serial.threaded.ReaderThread(ser, FakeArduino)
    protocol.start()
    
    print("✅ Fake Arduino running. Waiting for commands...")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("🛑 Stopping Fake Arduino...")
        protocol.stop()

if __name__ == "__main__":
    main()
