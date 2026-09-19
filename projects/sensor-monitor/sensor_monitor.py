import time
import RPi.GPIO as GPIO


SENSOR_PIN = 17
READ_INTERVAL = 1


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SENSOR_PIN, GPIO.IN)


def read_sensor():
    sensor_value = GPIO.input(SENSOR_PIN)

    if sensor_value:
        print("Sensor Status: DETECTED")
    else:
        print("Sensor Status: NOT DETECTED")


def main():
    print("Raspberry Pi Sensor Monitor")
    print("Press Ctrl+C to stop.\n")

    setup()

    try:
        while True:
            read_sensor()
            time.sleep(READ_INTERVAL)

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

    finally:
        GPIO.cleanup()


if __name__ == "__main__":
    main()