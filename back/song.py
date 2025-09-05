from back.item import Item
from back.thumbnail import get_thumbnail, Thumbnail
from back.ytm import YTM

class Song(Item):

	def __init__(self, id: str, title: str, url: str, artist: str, thumbnail: Thumbnail) -> None:
		self.id = id
		self.title = title
		self.url = url
		self.artist = artist
		self.thumbnail = thumbnail
		super().__init__("song")

	def __str__(self) -> str:
		res = f'~ {self.title}'
		res += f'\nid: {self.id}\nartist: {self.artist}\nurl: {self.url}'
		return res

def get_song(id: str) -> Song:
	song = YTM.get_song(id)
	return Song(
		id,
		song['videoDetails']['title'],
		song['microformat']['microformatDataRenderer']['urlCanonical'],
		song['videoDetails']['author'],
		get_thumbnail(song['microformat']['microformatDataRenderer']['thumbnail']['thumbnails'][0])
	)