import psutil

def main():
    memory_percent = psutil.virtual_memory().percent
    cpu_percent = psutil.cpu_percent()
    battery_percent = psutil.sensors_battery().percent if hasattr(psutil, 'sensors_battery') else None

    print(f"Memory Percent: {memory_percent}%")
    print(f"CPU Percent: {cpu_percent}%")
    if battery_percent is not None:
        print(f"Battery Percent: {battery_percent}%")
    else:
        print("Battery status not available.")

if __name__ == "__main__":
    main()
