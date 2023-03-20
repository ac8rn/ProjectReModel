#!/usr/bin/env python3
#created for use  of Enovation Controls
#this script uses a few open source libraries described below
#Author: August Nielsen (auggienielsen@gmail.com)
#some defines defined in the Neopixel strand test by Tony DiCola

#Made for use with the PV1100 

import time
from rpi_ws281x import *
import argparse
#import neopixel
#import board

#Raspberry Pi LED 
LEDcount     = 150      #number of LED pixels
LEDpin       = 18      #PWM pin 18
LEDfreq    = 800000  #sig freq in hz, 800 kHz
LEDdma       = 10      #DMA channel to gen signal
LEDbrightness = 60     #this is default, 0 darkest, 255 bright
LEDinvert     = False   #NPN factor
LEDchannel   = 0  # 1 for 13, 19, 41, 45, 53

#variables for user input
wait_ms1=50 #colorWipe speed
wait_ms2=150 #theatre chase mono and rainbow speed
wait_ms3=50 #rainbow speed

functionin=2 #describes which output is desired, chosen on PV1100
# 0 on, 1 wipe, 2 theatre chase, 3 rainbow, 4 theatre rainbow, 5 off

colorinr=60 #in red
colorinb=40 #in blue
coloring=200 #in green

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms1):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms1/1000.0)

def theaterChase(strip, color, wait_ms2, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms2/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)
                
def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms3, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms3/1000.0)

def theaterChaseRainbow(strip, wait_ms2):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms2/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def allOn(strip, color):
    """Turn all pixels to same color at once and leave on."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()

def allOff(strip, color=Color(0,0,0)):
    """Turn all pixels to same color at once and leave on."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()

# Main:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LEDcount, LEDpin, LEDfreq, LEDdma, LEDinvert, LEDbrightness, LEDchannel)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:

        while True:
            
            if functionin==0:
            #all on
                print ('all on')
                allOn(strip, Color(colorinr, colorinb, coloring))


            elif functionin==1:
                print ('wipe')
                colorWipe(strip, Color(colorinr, colorinb, coloring), wait_ms1)
                colorWipe(strip, Color(0, 0, 0), wait_ms1)
            #color wipe

            elif functionin==2:
                print ('chase')
                theaterChase(strip, Color(colorinr, colorinb, coloring), wait_ms2)
            #theatre chase

            elif functionin==3:
                print ('rainbow')
                rainbow(strip, wait_ms3)
            #rainbow

            elif functionin==4:
                print ('chase rainbow')
                theaterChaseRainbow(strip, wait_ms2)
            #theatre rainbow
                
            elif functionin==5:
                print ('off')
                allOff(strip)
                
            else:
                print ('error')
                

    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0), 10)