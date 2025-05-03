#made with <3 by lunatronia
#you can change the api key with your own but this is the default: b030404650f279792a8d3287232358e3
#v1.0.1

# TO-DO // add support for redirecting to series

import requests
import os
import time
from urllib.parse import quote_plus

apiKey = "b030404650f279792a8d3287232358e3"
gottenResponse = ""
print("welcome to tmdb-to-vidsrc! you can type \"help\" for a list of commands.")
while True:
    print("what would you like to do?")
    userCommand = input("> ")

    while True:
        if userCommand == "help":
            os.system("clear")
            print(f"current list of commands: \nhelp - displays this page \nwatch <query> - starts a search \nclear - clears console")
            userCommand = input("> ")
        else:
            if userCommand == "watch":
                userRequest = input("i wanna watch, ")
                break
            else:
                if userCommand == "clear":
                    os.system("clear")
                    userCommand = input("> ")
                else:
                    print("i didn't understand, can you type that again?")
                    userCommand = input("> ")

    userUrl = quote_plus(userRequest)
    print("searching...")
    os.system("clear")

    response = requests.get(f"https://api.themoviedb.org/3/search/multi?api_key={apiKey}&query={userUrl}")

# start display
    if response.status_code != 200:
        print(f"request failed with code {response.status_code}")
        exit()

    print("gotten results:")
    print("")

    data = response.json()

# filter valid results first
    validResults = []
    for result in data["results"]:
        mediaType = result.get("media_type", "")
        if mediaType in ["movie", "tv"]:
            validResults.append(result)

# print results with numbers
    for uid, result in enumerate(validResults, start=1):
        title = result.get("title") or result.get("name", "uhhhh")
        print(f"[{uid}] \ntitle:", title)
        print("overview:", result.get("overview", "it is something"))
        print("release date:", result.get("release_date", "some time"))
        print("vote average:", result.get("vote_average", "probably something"))
        print("id:", result.get("id", "i forgot"))
        print("")

# user choice
    if not validResults:
        print("no results, sorry")
        exit()

    while True:
        try:
            choice = int(input("i'll watch number "))
            if 1 <= choice <= len(validResults):
                selected = validResults[choice - 1]
                selectedTitle = selected.get("title") or selected.get("name")
                print(f"\nyou selected: {selectedTitle}")
                print(f"vidsrc link > https://vidsrc.rip/embed/movie/{selected.get('id')}")
                print(f"tmdb link > https://www.themoviedb.org/movie/{selected.get('id')}")
                break
            else:
                print("invalid choice")
        except ValueError:
            print("enter a proper number")

# more choice
    restart = input("\ndo you want to search again? (y/n): ").lower()
    if restart != "y":
        print("thanks for using tmdb-to-vidsrc!")
        break  # exit ;(
    else:
        os.system("clear")













