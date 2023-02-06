import requests
import os
import random
from bs4 import BeautifulSoup
import ctypes
from PIL import Image
import io
import datetime
import enum
import urllib.parse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Source(enum.Enum):
    pexels = 1
    unsplash = 2

search_term = "night"
mySource = Source.pexels
# mySource = Source.unsplash


options = Options()
options.headless = True
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")
dr = webdriver.Chrome(options=options)
# dr = webdriver.Chrome()

# Set the folder to save the wallpapers
wallpaper_folder = os.path.expanduser("~/Pictures/wallpapers")

# Create the folder if it doesn't exist
if not os.path.exists(wallpaper_folder):
    os.makedirs(wallpaper_folder)


if mySource == Source.unsplash:
    search_term = search_term.lower().strip().replace(" ","-")
    url = "https://unsplash.com/s/photos/"+search_term+"?orientation=landscape"
elif mySource == Source.pexels:
    search_term = search_term.lower().strip()
    search_term = urllib.parse.quote(search_term)
    url = "https://www.pexels.com/search/"+search_term+"?orientation=landscape"


# Use BeautifulSoup to scrape the page for image URLs
# soup = BeautifulSoup(requests.get(url).content, 'html.parser')
dr.get(url)
content = dr.page_source
soup = BeautifulSoup(content, 'html.parser')
a_tags = soup.find_all('a', href=True)
img_urls = [a['href'].split('?')[0] for a in a_tags if (a['href'].endswith("force=true") or a['href'].endswith("fm=jpg"))]

# img_urls = [a['href'].rstrip('force=true') for a in a_tags if a['href'].endswith("force=true")]

# Get the screen resolution
user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)
screen_ratio = screen_width / screen_height
print(screen_ratio)
print(len(img_urls))
# Download and check the resolution of each image
random.shuffle(img_urls)
for img_url in img_urls:
    print(img_url)
    # Extract the image name from the URL
    parts = img_url.split('/')
    img_name = parts[4]
    img_name = img_name + '.jpg'
    # Create the unique file name for the wallpaper
    image_path = os.path.join(wallpaper_folder, img_name)
    # Check if the image already exists in the folder
    if os.path.exists(image_path):
        # If the image already exists, skip to the next wallpaper
        print('Image already exists. Skipping...')
        continue
    with requests.get(img_url) as img_file:
        img = Image.open(io.BytesIO(img_file.content))
        width, height = img.size
        img_ratio = width / height
        print(img_ratio)
        print(width,height)
        # if img_ratio == screen_ratio and width>=screen_width and height>=screen_height:
        #     break
        if img_ratio > 1 and width>=screen_width and height>=screen_height:
            break

# Get the current desktop background image path
now = datetime.datetime.now()
# file_name = "wallpaper_{}.jpg".format(now.strftime("%Y-%m-%d_%H-%M-%S"))
image_path = os.path.join(wallpaper_folder, img_name)

# Save the image to the file path
img.save(image_path)

# Set the desktop background to the saved image
SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path , 0)
