import time
import Adafruit_DHT


SENSOR = Adafruit_DHT.DHT11
GPIO_PIN = 4
READ_INTERVAL = 2


def read_temperature():
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, GPIO_PIN)

    if temperature is None or humidity is None:
        print("Unable to read sensor data.")
        return

    print(
        f"Temperature: {temperature:.1f} °C | "
        f"Humidity: {humidity:.1f}%"
    )


def main():
    print("Raspberry Pi Temperature Monitor")
    print("Press Ctrl+C to stop.\n")

    try:
        while True:
            read_temperature()
            time.sleep(READ_INTERVAL)

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")


if __name__ == "__main__":
    main()