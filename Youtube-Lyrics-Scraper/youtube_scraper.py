from api_keys import yt_api_key as ytapi
from api_keys import lyricsgenius_api_key as lg
from youtube_api import YouTubeDataAPI
import lyricsgenius
import re

class Scraper:

    def __init__(self, name):
        self.name = name
        self.videos = []
        self.lyrics_text = []
        self.genius = lyricsgenius.Genius(lg)
        self.genius.verbose = False
        self.genius.remove_section_headers = True

    def youtube(self):
        yt = YouTubeDataAPI(ytapi)
        self.videos = yt.search(q=self.name, max_results=5)

        print("Last 5 videos for " + self.name)

        for i in range(5):
            video = self.videos[i]
            title = re.sub(r" ?\([^)]+\)", "", video["video_title"])
            if "&#39;" in title:
                title = title.replace("&#39;", "'")
                if "And" in title:
                    title = title.replace("And", "&")
            print("#" + str(i+1) + ": " + title)
            print("https://youtu.be/" + video["video_id"])
            song = self.genius.search_song(title.replace(name + " - ", ""), self.name)
            print(song.lyrics + "\n")

name = input("Please enter the artist's name: ")
scraper = Scraper(name)
scraper.youtube()

