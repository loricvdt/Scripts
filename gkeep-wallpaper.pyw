import ctypes
import gkeepapi
from PIL import Image, ImageDraw, ImageFont

#### CHANGE HERE ####
# Gkeepapi credentials
keep_email = ""
keep_token = ''
# Google keep list ID (in Google Keep URL)
list_ID = ""

# Location of the original wallpaper (never overwritten)
default_wp_path = ""
# Suffix added to the original to write list
KEEP_SUFFIX = "_keep.png"

# Visual settings (position, colour, font, ...)
font = ImageFont.truetype("verdana.ttf", 14)
text_colour = (0, 0, 0)
background_colour = (255, 255, 255)
list_pos = (1300, 100)
margin = 10
#####################


def set_wallpaper(path):
	ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)


def connect_keep():
	_keep = gkeepapi.Keep()
	_keep.resume(keep_email, keep_token)
	return _keep


def draw_list(_img, items):
	max_width = 0
	max_height = 0
	for item in items:
		size = font.getsize("- " + item.text)
		if size[0] > max_width:
			max_width = size[0]
		if size[1] > max_height:
			max_height = size[1]

	d = ImageDraw.Draw(_img)
	d.rectangle((list_pos, (list_pos[0] + max_width + margin * 2, list_pos[1] + max_height * len(items) + margin * 2)),
				background_colour)

	for i in range(len(items)):
		d.text((list_pos[0] + margin, list_pos[1] + margin + i * max_height), "- " + items[i].text, fill=text_colour,
			   font=font)


if __name__ == '__main__':
	default_wp = Image.open(default_wp_path)

	keep = connect_keep()
	note = keep.get(list_ID)

	img = default_wp.copy()

	draw_list(img, note.unchecked)

	img.save(default_wp_path + KEEP_SUFFIX)
	set_wallpaper(default_wp_path + KEEP_SUFFIX)
