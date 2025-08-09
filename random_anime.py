import requests
from rich.console import Console
from rich.prompt import Prompt
from ascii_magic import AsciiArt



def get_random_anime():
    with console.status("Fetching Data...,", spinner="material"):
        request = requests.get("https://api.jikan.moe/v4/random/anime")
        request_json = request.json()
        data = request_json["data"]
        if request.status_code != 200:
            return 
        else:
            images = data["images"]
            webps = images["webp"]
            return (data["title"],data["score"],data["scored_by"],data["rank"],data["popularity"],webps["image_url"])
             
    
    
    
def make_ascii_art(url:str):
    try:
        ascii_art = AsciiArt.from_url(url)
        return ascii_art.to_ascii()
    except Exception as error:
        print(f"Couldn't convert image to ascii, error: {error}")
    

if __name__ == "__main__":
    console = Console()
    console.rule("[bold red] Random Anime")
    console.print("Welcome to Random Anime\nType 'q' to quit or 'y' for a random anime !",justify="center")
    while True:
        command = Prompt.ask("Show random anime ?:\n>",case_sensitive=False, choices=["y","n"], default="y")
        if command == "y":
            request_output = get_random_anime()
            print_anime_presentation(request_output)
        else:
    