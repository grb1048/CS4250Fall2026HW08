import smbus2
import time
import subprocess

BUS_ID = 1
DEVICE_ADDRESS = 0x68
LED_GPIO_PIN = 405  # Change this to match your new pin's GPIO number

def setup_led():
    subprocess.run(f"echo {LED_GPIO_PIN} > /sys/class/gpio/export 2>/dev/null", shell=True)
    subprocess.run(f"echo out > /sys/class/gpio/gpio{LED_GPIO_PIN}/direction", shell=True)

def set_led(state):
    val = "1" if state else "0"
    subprocess.run(f"echo {val} > /sys/class/gpio/gpio{LED_GPIO_PIN}/value", shell=True)

def init_sensor(bus):
    try:
        bus.write_byte_data(DEVICE_ADDRESS, 0x6B, 0x00)
        return True
    except Exception:
        return False

setup_led()
bus = smbus2.SMBus(BUS_ID)
print("Initializing MPU6050 tilt-activated LED...")

while not init_sensor(bus):
    time.sleep(1)

print("Running! Tilt the board to light the LED. (Ctrl+C to exit)")

try:
    while True:
        high = bus.read_byte_data(DEVICE_ADDRESS, 0x3B)
        low = bus.read_byte_data(DEVICE_ADDRESS, 0x3C)
        
        accel_x = (high << 8) | low
        if accel_x & 0x8000:
            accel_x -= 65536

        # Light LED when tilted past threshold
        if abs(accel_x) > 3000:
            set_led(True)
            print(f"Accel X: {accel_x}  ---> TILT! LED ON")
        else:
            set_led(False)
            print(f"Accel X: {accel_x}")
            
        time.sleep(0.1)
        
except KeyboardInterrupt:
    set_led(False)
    print("\nExiting...")