import sys
import requests
import os
from zipfile import ZipFile

def album_zip_downloader(album_url, saveLocation):
    if not os.path.exists(saveLocation):
        os.makedirs(saveLocation)
    file_data = requests.get(album_url).content
    with open(f"{saveLocation}/album.zip", "wb") as file:
        file.write(file_data)
    with ZipFile(f"{saveLocation}/album.zip", 'r') as zipObject:
        zipObject.extractall(f"{saveLocation}")
    os.remove(f"{saveLocation}/album.zip")

def convert_to_zip_url(imgur_gallery_url):
    # Extract the gallery ID from the original URL
    parts = imgur_gallery_url.split('/')
    gallery_id = parts[-1]

    # Construct the new URL
    zip_url = f'https://imgur.com/a/{gallery_id}/zip'
    
    return zip_url

#main
if len(sys.argv) == 2:
    print(f"Grabbing ", sys.argv[1])
    album_url = convert_to_zip_url(sys.argv[1])
    saveLocation = "C:/Users/Donnie/Pictures/Wallpapers"
    print(f"saving {album_url} to {saveLocation}")
    album_zip_downloader(album_url, saveLocation)
if len(sys.argv) > 2:
    print(f"Grabbing ", sys.argv[1])
    album_url = convert_to_zip_url(sys.argv[1])
    saveLocation = sys.argv[2]
    print(f"saving {album_url} to {saveLocation}")
    album_zip_downloader(album_url, saveLocation)
