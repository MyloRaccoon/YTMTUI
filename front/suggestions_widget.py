from back.album import Album
from back.artist import Artist
from back.suggestions import Suggestions
from front.album_widget import AblumWidget
from front.artist_widget import ArtistWidget
from front.playlist_widget import PlaylistWidget
from front.song_widget import SongWidget
from textual.app import ComposeResult
from textual.widget import Widget
from textual.containers import HorizontalScroll

class SuggestionsWidget(Widget):

	def __init__(self, suggestions: Suggestions) -> None:
		self.suggestions = suggestions
		super().__init__()

	def compose(self) -> ComposeResult:
		with HorizontalScroll():
			for suggestion in self.suggestions.suggestions:
				yield SongWidget(suggestion)
				# match suggestion.item_type:
				# 	case 'album': yield AblumWidget(suggestion)
				# 	case 'artist': yield ArtistWidget(suggestion)
				# 	case 'playlist': yield PlaylistWidget(suggestion)
				# 	case 'song': yield SongWidget(suggestion)

	def on_mount(self) -> None:
		self.border_title = self.suggestions.title
