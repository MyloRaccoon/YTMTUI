from back.item import Item
from back.thumbnail import Thumbnail, get_thumbnail
from back.ytm import YTM

class Playlist(Item):

	def __init__(self, id: str, title: str, description: str, author_id: str, thumbnail: Thumbnail, tracks: list[str]) -> None:
		self.id = id
		self.title = title
		self.description = description
		self.author_id = author_id
		self.thumbnail = thumbnail
		self.tracks = tracks
		super().__init__("playlist")

	def __str__(self) -> str:
		res = f'~ {self.title}'
		res += f'\ntype: playlist\ndesc: {self.description}'
		return res

def get_playlist(id: str) -> Playlist:
	pl = YTM.get_playlist(id)
	return Playlist(
		id,
		pl['title'],
		pl['description'],
		pl['author']['id'],
		get_thumbnail(pl['thumbnails'][0]),
		[song['videoId'] for song in pl['tracks']]
)