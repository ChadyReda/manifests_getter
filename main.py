from steam_utils import get_game_id, get_manifest_download_file, download_and_extract_zip
from rich.console import Console
from art import tprint


console = Console()
tprint("chady code")
print("chady/lorax Team")
print("")
console.print("🛠️  - chadyxreda@gmail.com", style="underline")
print("")



while True:
    gameName = input("Enter the game name > ")
    print("▼")
    gameId = get_game_id(gameName)

    if gameId:
        console.print(f"Id found {gameId}", style="green")
        print("▼")
        # Await the asynchronous get_manifest_download_file
        manifest_response = get_manifest_download_file(gameId)
        if manifest_response:
            console.print(f"Successfully got the manifests files for ", style="green", end="")
            console.print(gameName, style="blue underline")
            print("▼")
            download_and_extract_zip(gameName, manifest_response['url'])
            console.print("downloaded successefully", style="cyan bold")
            print("▼")
            console.print("check the downloads folder in the project root to find manifets", style="blue underline")
            print("▼")
            console.print("Add another game you like 🤫", style="grey66 underline")
            print("")
    else:
        console.print("Game Not found ", style="yellow bold underline", end="")
        console.print("-copy game name from steam-", style="blue_violet")
        print("")
