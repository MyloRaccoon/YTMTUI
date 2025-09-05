from back.item import Item
from back.thumbnail import get_thumbnail, Thumbnail
from back.ytm import YTM

class Album(Item):

	def __init__(self, id: str, title: str, description: str, artist_id: str, thumbnail: Thumbnail, tracks: list) -> None:
		self.id = id
		self.title = title
		self.description = description
		self.artist_id = artist_id
		self.thumbnail = thumbnail
		self.tracks = tracks
		super().__init__("album")

	def __str__(self) -> str:
		res = f'~ {self.title}'
		res += f'\ntype: album\ndesc: {self.description}\nurl: {self.id}'
		return res

def get_album(id: str) -> Album:
	album = YTM.get_album(id)
	return Album(
		id,
		album['title'],
		album['description'],
		album['artists'][0]['id'],
		get_thumbnail(album['thumbnails'][0]),
		[track['videoId'] for track in album['tracks']]
	)