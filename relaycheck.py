import RPi.GPIO as GPIO
import time
import board
import adafruit_dht

channel = 18

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)
dhtDevice = adafruit_dht.DHT11(board.D4)
temperature_c = dhtDevice.temperature
print("{:.1f}"
.format(temperature_c))
GPIO.input(channel)
channel_is_on = GPIO.input(channel)

print (channel_is_on)
def relay_on(pin):
    GPIO.output(pin, GPIO.HIGH)  # Turn relay on
def relay_off(pin):
    GPIO.output(pin, GPIO.LOW)  # Turn relay off
def tempinrange():
        print("{:.2f}"
.format(temperature_c))
        print ("temperature Above 25 Degrees - NO heater required")
def tempoutofrange():
        print("{:.2f}"
.format(temperature_c))
        print ("temperature Below 25 Degrees - Heater required")

if channel_is_on == 0:
        if temperature_c >= 25:
                tempinrange()
        else:
                tempoutofrange()
                time.sleep(2)
                relay_on(channel)
                print ("Heater Turned on")
else:
        if temperature_c >= 25:
                tempinrange()
                time.sleep(2)
                relay_off(channel)
        else:
                tempoutofrange()
                print ("Heater Kept on")    
