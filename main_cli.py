from back.home import Home
from back.player import play


print("retrieving songs")
home = Home()
song = home.suggestions[0]
print(f"playing: {song.title}")
play(song)

