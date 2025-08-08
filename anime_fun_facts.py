import requests
import rich
from ascii_magic import AsciiArt
import random

def get_random_anime():
    request = requests.get("https://api.jikan.moe/v4/random/anime")
    request_json = request.json()
    data = request_json["data"]
    if request.status_code == 200:
        images = data["images"]
        webps = images["webp"]
        return data["title"],data["score"],data["scored_by"],data["rank"],data["popularity"],webps["large_image_url"]
    else:
        return -1
    
    
    
def draw_ascii_image(url:str):
    try:
        ascii_art = AsciiArt.from_url(url)
        return ascii_art.to_ascii()
    except Exception as error:
        print(f"Couldn't load image, error name: {error.__str__}")
    

if __name__ == "__main__":
    get_random_anime()