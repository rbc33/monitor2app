
import os
import time
import psutil
import sys

def clear_screen():
    os.system('clear')  # For macOS and Linux

def main():
    while True:
        memory_percent = psutil.virtual_memory().percent
        cpu_percent = psutil.cpu_percent()
        battery_percent = psutil.sensors_battery().percent if hasattr(psutil, 'sensors_battery') else None

        clear_screen()  # Clear the entire console screen

        print(f"Memory Percent: {memory_percent}%")
        print(f"CPU Percent: {cpu_percent}%")

        if battery_percent:
            print(f"Battery Percent: {battery_percent}%")
        else:
            print("Battery status not available.")

        time.sleep(0.5)  # Wait for 0.5 seconds before the next update

if __name__ == "__main__":
    main()
