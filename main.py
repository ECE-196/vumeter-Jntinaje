# Write your code here :-)
import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)  # This is still included for potential future use
status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT


led_pins = [
    board.IO21,
    board.IO26,  # type: ignore
    board.IO47,
    board.IO33,  # type: ignore
    board.IO34,  # type: ignore
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

def LEDStatus(volume,LedOns):
    for idx in range(len(leds)):
        leds[idx].value = idx < LedOns
    
# main loop
while True:
    volume = microphone.value
    uppBound=27000
    increment = (uppBound/len(leds))
    start = 22000
    LedOns = min(int((volume - start)/increment), len(leds))
    LEDStatus(volume,LedOns)
    print(volume)
    sleep(1)