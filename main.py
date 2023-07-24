from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from os import system
import signal
import sys

import psutil

import time
from datetime import datetime

# VARS

fontname   = "Hack-Regular.ttf" # Font (must be in same directory)
width      = 64 # Image width
height     = 36 # Image height
command    = "asusctl anime pixel-gif -p pixel.gif" # Command to be run every minute. Make sure the -p is the same as the filename. Put all your fine tweaking here.
textcolour = (255, 255, 255) # Text colour
refresh    = 1 # Time in seconds between refreshes
keybind    = 269025089 # XF86Launch3

# END VARS

font = ImageFont.truetype(fontname, 10) # Register large font
W,H = (width, height)

active = True

def main():
	now = datetime.now() # Get the current time
	strtime = now.strftime("%H:%M:%S") # Get time string
	strdate = now.strftime("%d.%m.") # Get date string
	strbattery = str(round(psutil.sensors_battery().percent)) + "%" # Get battery level in percent

    # Create new image
	img = Image.new("RGB", (width, height))
	draw = ImageDraw.Draw(img)

	# For development: Calculcate size and centered position.
	#w = fonts.getmask(strbattery).getbbox()[2]
	#h = fonts.getmask(strbattery).getbbox()[3]
	#print("Width and height:", w, h)
	#print("Calculated centered position:", (W-w)/2, (H-h)/1.1)

	# Draw text
	draw.text((8.0, 26.5), strtime, textcolour, font=font) # Time
	draw.text((17.5, 17.25), strdate, textcolour, font=font) # Date
	draw.text((25.5, 8.0), strbattery, textcolour, font=font) # Battery

	img.save("pixel.gif")

	system(command) # Update matrix

def cleanup(signal, frame):
	system("asusctl anime -e false") # Turn off matrix on sigint
	sys.exit(0)

if __name__ == "__main__":
	system("asusctl anime -e true") # Enable display
	system("asusctl anime -i 0.5") # Set brightness
	signal.signal(signal.SIGINT, cleanup) # Register SIGINT handler
	while True:
		if active :
			main()
		time.sleep(refresh - time.time() % refresh) # Run at the start of every $refresh second
