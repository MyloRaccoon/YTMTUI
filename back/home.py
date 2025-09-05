from back.song import Song
from back.thumbnail import Thumbnail
from back.ytm import YTM
import random

LIMIT = 20

class Home:

	def __init__(self):
		self.suggestions = []
		self.get_suggestions()

	def get_suggestions(self):
		recent_songs = YTM.get_history()[0:20]
		recent_tracks = []
		for item in recent_songs:
			if "videoId" in item:
				recent_tracks.append({
					"title": item.get("title"),
					"artist": item.get("artists", [{"name": ""}])[0]["name"],
					"videoId": item["videoId"]
				})

		recommendations = []
		for track in recent_tracks[:10]:
			related = YTM.get_watch_playlist(track["videoId"], limit=3)['tracks']
			for r in related:
				recommendations.append({
					"title": r.get("title"),
					"artist": r.get("artists", [{"name": ""}])[0]["name"],
					"videoId": r.get("videoId")
				})

		home_feed = recent_tracks + recommendations
		random.shuffle(home_feed)
		
		for json in home_feed:
			self.suggestions.append(
				Song(
					json['videoId'], 
					json['title'], 
					'a', 
					json['artist'], 
					Thumbnail('a', 0, 0)
				)
			)

	def __str__(self) -> str:
		res = '~~~~~~~~~~ YTMCLI ~~~~~~~~~~'
		for song in self.suggestions:
			res += song.__str__()
		return res

