from back.ytm import get_account_name
from textual.widget import Widget
from textual.widgets import Label
from textual.app import ComposeResult
from textual.containers import Grid, Horizontal, VerticalScroll, HorizontalScroll
from front.album_widget import AblumWidget
from front.artist_widget import ArtistWidget
from front.playlist_widget import PlaylistWidget
from front.song_widget import SongWidget

class HomeWidget(Widget):

	def __init__(self, home):
		self.home = home
		super().__init__()

	def compose(self) -> ComposeResult:
		songs = self.home.suggestions.copy()
		with VerticalScroll():
			with Grid():
				for song in songs[:30]:
					yield SongWidget(song)

			# match suggestion.item_type:
			# 	case 'album': yield AblumWidget(suggestion)
			# 	case 'artist': yield ArtistWidget(suggestion)
			# 	case 'playlist': yield PlaylistWidget(suggestion)
			# 	case 'song': yield SongWidget(suggestion)
