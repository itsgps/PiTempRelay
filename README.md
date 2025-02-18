# PiTempRelay
Python script to trigger Relay Open/Close on Raspberry with Arduino Relay

This script uses the temperature of a DHT11 (or DHT22 for more precision.) to determine the current temperature.  The DHT11 for instance should have 3 pins normally, 5V, GND and IO - the Data pin - with the specifically provided script we plug the Data pin into GPIO pin 4 on a Raspberry Pi 2,3,4,5, Zero, etc.

Import the appropriate Libraries for access to the DHT unit (they can vary depending on which Version of OS or Pi you are using - but as an example it might be:

sudo pip3 install Adafruit_DHT
sudo pip3 install Adafruit_CircuitPython_DHT
sudo apt install libgpiod*   - For access to GPIO on the Pi***
sudo pip3 install Adafruit_CircuitPython_bmp280
sudo pip3 install adafruit-circuitpython-busdevice
sudo pip3 install smbus2

***You also need to enable GPIO Pins in the raspi-config.

Next Connect the Data pin of an Arduino Relay to Pin 18  (or any available) and power it from the same 5V supply to the Pi.  Keep in mind, if you do not have a sufficient 5V power supply to the Pi (i.e. just powering it via a standard USB A Micro connection, which might only deliver up to 500mA - you will find that there is not enough output from the Pi itself, and when the Relay is triggered, often this can cause a Significant Undervolt condition on the Pi and cause it to reboot.  So powering your Pi from a PoE Pi Hat, or adding external 5v from say a 12v > 5v converter usually avoids this.

This script can be used for any Temp/Relay control really - but ostensibly it was written to control a Dew Heater for Astro cameras.  So just to note further, once you have the above setup, you also connect a 12v Line (positive only) to the NO (Normally Open) lines of the relay, with the other end going to your Dew Heater.  Which has it's Negative line directly connected to the Negative line of that same Power supply.

When Set temperature is reached - the Relay will CLOSE, and the 12v line to the Dew heater will become active.
I have found that for AllSky Cameras - setting the Detected temperature to at least 5 to 10 degrees above the Nominal Dew point give the Dome of the All Sky camera time to warm up and prevent External as well as Internal Dewing.

The script itself can be run independantly to anything else running on the Pi (such as Allsky software) as a Cron job running every 20 minutes in order to turn on at a time when appropriate to prevent Dew.

If using this method, inclusive of using a DHT11, or DHT22 sensor - this allows you to check the Temperature Closer to the Dome if your Pi is not Completely Close to the dome itself.  You also have to make sure you account for how Internal temperature is considered.  I.e. as we Now turn on the Heater, are we heating the enclosure to the point where the Heater will turn off...and prevent clearing Dew.  The System for the most part will nominally counter this if you are in an environment which drops temperature fast.  Mainly because the Dew Heater is not usually powerful enough to prevent the outside environment from making the inside enclosure too hot when the temperature drops rapidly.  As such - you may find the heater goes on to begin with...then turns off in the next 20 min cycle...but then next time it goes on for 40 mins...then turns off...but by the next cycle, 1 hour has passed since it first turned on, so temp will likely have dropped enough that the Next Power on - will remain until Morning, and so on.

The Below is an example CronTab entry.

0,20,40 * * * * python3 /home/user/allsky/relaycheck.py | mailx -s "AllSky Relay check" user@example.com

Hope this Helps anyone out there.

Regards

Leigh

