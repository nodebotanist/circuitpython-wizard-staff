import board
import time
import neopixel
from adafruit_circuitplayground.express import cpx

cpx.detect_taps = 2

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)
pixels.fill((0, 0, 0))
pixels.show()

while True:
  if cpx.tapped:
    pixels.fill((102, 51, 153))
    pixels.show()
    time.sleep(1)
    pixels.fill((0, 0, 0))
    pixels.show()

  if cpx.button_a:
    print("Button A")

  if cpx.button_b:
    print("Button B")

  time.sleep(.1)