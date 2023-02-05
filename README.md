# BackgroundBazaar

BackgroundBazaar is a Python script that automatically changes the wallpaper on your Windows desktop based on a search term. It searches Unsplash.com and Pexels.com, downloads a random wallpaper matching the search term, and sets it as your desktop background. With BackgroundBazaar, you can easily freshen up your desktop and add a personal touch to your workspace.

## Features
- Searches for wallpapers based on a search term on Unsplash.com and Pexels.com
- Downloads the selected wallpaper and sets it as the desktop background
- Maintains an archive of the downloaded wallpapers on your computer

## Requirements
- Python 3
- Beautifulsoup4
- Pillow
- Requests
- Selenium

## Installation
To install the required modules, run the following command in your terminal:
```
pip install -r requirements.txt
```

## Usage
To run BackgroundBazaar, simply enter the search term and specify one of the wallpaper sources (Unsplash or Pexels) in the script. Then run the script using the command `python background_bazaar.py`. The script will download a random wallpaper matching the search term and set it as your desktop background.

## Future Plans
In the future, we plan to add a user-friendly UI to make it even easier to use BackgroundBazaar.

## License
BackgroundBazaar is licensed under the MIT License.

## Contribute
We welcome contributions to BackgroundBazaar! If you have a bug fix or new feature, please open a pull request. For major changes, please open an issue first to discuss what you would like to change.
