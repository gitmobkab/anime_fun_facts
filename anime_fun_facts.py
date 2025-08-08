import requests
import rich
from ascii_magic import AsciiArt
import random

def get_random_anime(numbers_of_requests: int = 1):
    request = requests.get("https://api.jikan.moe/v4/random/anime")
    request_json = request.json()
    data = request_json["data"]
    if request.status_code == 200:
        images = data["images"]
        webps = images["webp"]
        draw_ascii_image(webps["large_image_url"])
        return data["title"],data["score"],data["score_by"],data["rank"],data["popularity"]
    else:
        return 0
    
    
    
def draw_ascii_image(url:str):
    try:
        ascii_art = AsciiArt.from_url(url)
        ascii_art.to_terminal()
    except Exception as error:
        print(f"Couldn't load image, error name: {error.__str__}")
    
get_random_anime()