import requests
from bs4 import BeautifulSoup
import zipfile
import os
from rich.console import Console

console = Console()

def get_game_id(game_name):
    try:
        # Format the search URL with the game name
        search_url = f"https://store.steampowered.com/search/?term={game_name.replace(' ', '+')}"
        response = requests.get(search_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the first game result and extract the appid
        results = soup.find_all('a', href=True)
        for result in results:
            href = result['href']
            if 'store.steampowered.com/app/' in href:
                # Only return the game ID, without the name
                game_id = href.split('/app/')[1].split('/')[0]
                return game_id
        return None
    except:
        console.print(f"Error getting the Id for {game_name}", style="orange_red1 underlined")



def get_manifest_download_file(game_id):
    try:
        generate_url = f"https://vinn-web-tools-dandys-projects-bb4af0ab.vercel.app/get-appid?appid={game_id}"
        download_url = f"https://vinn-web-tools-dandys-projects-bb4af0ab.vercel.app/download?appid={game_id}"

        generate_response = requests.get(generate_url)
        if generate_response.status_code == 200:
            manifest_response = requests.get(download_url)
            return manifest_response.json()
        else:
            print(f"Manifest not found! -- failed with status code: {generate_response.status_code}")
            return None
    except:
        console.print("Error getting Manifests ⚠️", style="orange_red1 underline")
        print("")


def download_and_extract_zip(game_name, url):
    # Ensure the game_id is properly converted to string 
    try:
        # Create the main download path if it doesn't exist
        download_path = 'downloads'
        if not os.path.exists(download_path):
            os.makedirs(download_path)
        
        # Create a subfolder named after the game_id
        game_folder_path = os.path.join(download_path, game_name)
        if not os.path.exists(game_folder_path):
            os.makedirs(game_folder_path)
        
        # Download the zip file
        response = requests.get(url)
        zip_path = os.path.join(game_folder_path, 'downloaded.zip')
        
        # Write the content to a file
        with open(zip_path, 'wb') as zip_file:
            zip_file.write(response.content)
        
        # Extract the zip file
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(game_folder_path)
        
        # Remove the zip file after extraction
        os.remove(zip_path)
    except:
        console.print("Error Downloading Manifests! -🛈 check your network connection or try again 🛈-", style="red1 underline")
        print("")


def get_dlc():
    