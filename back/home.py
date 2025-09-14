from back.song import Song, song_from_data
from back.thumbnail import Thumbnail
from back.ytm import YTM
import random
import json
import time
import os

LIMIT = 20

HOME_DELAY = 30

POOL_PATH = 'home_pool.json'

def home_loop():
	while True:
		time.sleep(HOME_DELAY)
		push_home()


def push_home():
	home_data = Home().new().to_data()

	if not os.path.isfile(POOL_PATH):
		pool = []
	else:
		with open(POOL_PATH, 'r') as f:
			pool = json.load(f)

	if not isinstance(pool, list):
		pool = []

	pool.append(home_data)
	with open(POOL_PATH, 'w') as f:
		f.write(json.dumps(pool))

def pull_home():
	
	if not os.path.isfile(POOL_PATH):
		return Home().new()

	with open('home_pool.json', 'r') as f:
		pool = json.load(f)

	if (not isinstance(pool, list)) or len(pool) == 0:
		return Home().new()
	else:
		home_data = pool.pop(-1)
		with open('home_pool.json', 'w') as f:
			f.write(json.dumps(pool))
		return Home().from_data(home_data)

class Home:

	def __init__(self):
		self.suggestions = []

	def new(self):
		self.get_suggestions()
		return self

	def from_data(self, data):
		for song in data:
			self.suggestions.append(
				song_from_data(song)
			)
		return self

	def to_data(self) -> list[dict]:
		return [song.to_data() for song in self.suggestions]

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

