from back.item import Item
from back.thumbnail import get_thumbnail, Thumbnail
from back.ytm import YTM

class Artist(Item):

	def __init__(self, id: str, name: str, description: str, subscribers: str, subscribed: bool, thumbnail: Thumbnail, songs: list[str], albums: list[str], singles: list[str], videos: list[str]):
		self.id = id
		self.name = name
		self.description = description
		self.subscribers = subscribers
		self.subscribed = subscribed
		self.thumbnail = thumbnail

		self.songs = songs
		self.albums = albums
		self.singles = singles
		self.videos = videos

		super().__init__("artist")

	def __str__(self) -> str:
		res = f'~ {self.name}'
		res += f'\ntype: user\ndesc: {self.description}'
		return res

def get_artist(id: str) -> Artist:
	artist = YTM.get_artist(id)
	songs = [song['videoId'] for song in artist['songs']['results']]
	albums = [album['browseId'] for album in artist['albums']['results']]
	singles = [single['browseId'] for single in artist['singles']['results']]
	videos = [video['videoId'] for video in artist['videos']['results']]
	return Artist(
		id,
		artist['name'],
		artist['description'],
		artist['subscribers'],
		artist['subscribed'],
		get_thumbnail(artist['thumbnails'][0]),

		songs,
		albums,
		singles,
		videos
	)