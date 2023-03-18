#include <math.h>
#include <stdio.h>

//Raspberry Pi LED 
LEDcount     = 150      //number of LED pixels
LEDpin       = 18      //PWM pin 18
LEDfreq    = 800000  //sig freq in hz, 800 kHz
LEDDMA       = 10      //DMA channel to gen signal
LEDbrightness = 50     //Set to 0 for darkest and 255 for brightest
LEDinvert     = False   //NPN factor
LEDchannel   = 0  // 1 for 13, 19, 41, 45, 53

int r = 255;
int g = 255;
int b = 255;


void main()
{
    while(1){
          //print ('Color wipe animations.')
            colorWipe(strip, Color(255, 0, 0))  # Red wipe
            colorWipe(strip, Color(0, 255, 0))  # Blue wipe
            colorWipe(strip, Color(0, 0, 255))  # Green wipe
            //print ('Theater chase animations.')
            theaterChase(strip, Color(127, 127, 127))  # White theater chase
            theaterChase(strip, Color(127,   0,   0))  # Red theater chase
            theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
           // print ('Rainbow animations.')
            rainbow(strip)
            rainbowCycle(strip)
            theaterChaseRainbow(strip)
  //wipe color across strip one pixel at a time
        //for i
 ]
   
}

void colorWipe(strip, color, waitTime)

