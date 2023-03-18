#created for use  of Enovation Controls
#this script uses a few open source libraries described below
#Author: August Nielsen (auggienielsen@gmail.com)
#some defines defined in the Neopixel strand test by Tony DiCola

#Made for use with the PV1100 

import time
from rpi_ws281x import *
import argparse
import neopixel
import board

#Raspberry Pi LED 
LEDcount     = 150      #number of LED pixels
LEDpin       = 18      #PWM pin 18
LEDfreq    = 800000  #sig freq in hz, 800 kHz
#LEDDMA       = 10      #DMA channel to gen signal
LEDbrightness = 50     #this is default
LEDinvert     = False   #NPN factor
LEDchannel   = 0  # 1 for 13, 19, 41, 45, 53

#variables for user input
functionin=0 #describes which output is desired, chosen on PV1100
colorinr=0 #in red
colorinb=0 #in blue
coloring=0 #in green

#variables for output 
x=0 #keeps count of LEDs

#for addressing entire strip at once, input is GPIO pin, number of LEDs, and brightness level
#pixels1 = neopixel.NeoPixel(board.D18, 55, brightnessin)

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def allOn(strip, color):
    """Turn all pixels to same color at once and leave on."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:

        while True:
            
            if functionin==0
            #all on
            allOn(strip, Color(colorinr, colorinb, coloring))


            elif functionin==1
            colorWipe(strip, Color(colorinr, colorinb, coloring))
            #color wipe

            elif functionin==2
            theaterChase(strip, Color(colorinr, colorinb, coloring))
            #theatre chase

            elif functionin==3
            rainbow(strip, Color(colorinr, colorinb, coloring))
            #rainbow

            elif functionin==4
            rainbowCycle(strip, Color(colorinr, colorinb, coloring))
            #rainbow cycle

            elif functionin==5
            theaterChaseRainbow(strip, Color(colorinr, colorinb, coloring))
            #theatre rainbow



    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0), 10)