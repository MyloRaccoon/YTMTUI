from back.playlist import get_playlist
from back.song import Song, get_song
from back.album import get_album
from back.artist import get_artist
from back.thumbnail import Thumbnail

class Suggestions:

	def __init__(self, title: str, items: list[dict]):
		self.title = title
		self.suggestions = []
		for json in items:
			self.suggestions.append(Song(json['videoId'], json['title'], 'a', json['artist'], Thumbnail('a', 0, 0)))
		# for suggestion in json['contents']:
		# 	self.suggestions.append(get_suggestion(suggestion))

	def __str__(self) -> str:
		res = f"\n	~~~ {self.title} ~~~"
		for suggestion in self.suggestions:
			res += suggestion.__str__()
			res += '\n---\n'
		return res

def get_suggestion(json: dict):
	if 'videoId' in json.keys():
		return get_song(json['videoId'])

	elif 'playlistId' in json.keys():
		return get_playlist(json['playlistId'])

	elif 'subscribers' in json.keys():
		return get_artist(json['browseId'])

	else:
		return get_album(json['browseId'])
