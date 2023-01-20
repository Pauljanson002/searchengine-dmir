import pandas as pd
import requests
from bs4 import BeautifulSoup
data = []

main_lyrics_site = "https://tamilsonglyrics4u.com/a-to-z.html"
def main():
    for i in range(50):
        print(f"Enter song details {(len(data) + 1)} : ")
        name = input("Name of song : ")
        if name == "exit":
            break
        lyrics = input("Lyrics url : ")
        composer = "ஹாரிஸ் ஜெயராஜ்"
        lyricist = input("Lyricist : ")
        album = input("Album : ")
        singer = input("Singer : ")
        year = input("Year : ")
        metaphor = input("Metaphor : ")
        
        page = requests.get(lyrics)
        soup = BeautifulSoup(page.content, 'html.parser')
        p_tags = soup.find_all("p")
        lyrics_content = p_tags[1].text.replace("\n", "") 
        
        print("Done")
        
        song_data = {
            "name": name,
            "lyrics": lyrics_content,
            "composer": composer,
            "lyricist": lyricist,
            "album": album,
            "singer": singer,
            "year": year,
            "metaphor": metaphor,
        }
        data.append(song_data)
        pd.DataFrame(data).to_csv("songs.csv", index=False)

if __name__ == "__main__":
    main()
    