import board
import neopixel
import time

# Define the colors as RGB tuples
colors = [
    (0, 255, 0),    # Red
    (255, 50, 255),  # Aqua
    (255, 0, 0),    # Green
    (0, 0, 255),    # Blue
    (100, 255, 0),  # Amber
    (50, 255, 255), # Aqua
    (255, 0, 255),  # Cyan
    (183, 188, 38), # Gold
    (255, 0, 40),   # Jade
    (0, 255, 20),   # Magenta
    (134, 4, 235),  # Marine
    (40, 255 , 0),  # Orange
    (15, 239, 127), # Pink
    (255, 4, 105),  # Mint
    (189, 4, 255),  # Baby Blue
    (259, 89, 6),   # Lime
    (255, 165, 0),  # Orange
    (128, 0, 128),  # Purple
    (0, 255, 255),  # Teal
    (255, 215, 0),  # Gold
    (0, 128, 0),    # Forest Green
    (255, 192, 203),# Pink
    (70, 130, 180), # Steel Blue
    (255, 69, 0),   # Orange-Red
    (220, 20, 60),  # Crimson
    (0, 139, 139),  # Dark Cyan
    (255, 20, 147), # Deep Pink
    (0, 0, 128),    # Navy
    (255, 105, 180),# Hot Pink
    (123, 104, 238),# Medium Orchid
    (32, 178, 170)  # Light Sea Green
]

num_pixels = 8
brightness = 0.5
speed = 5

pixels = neopixel.NeoPixel(board.GP22, num_pixels, pixel_order="RGB")
pixels.brightness = brightness

while True:
    for color in colors:
        pixels.fill(color)
        time.sleep(speed)