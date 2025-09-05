from back.playlist import Playlist
from back.artist import get_artist
from front.suggestion_item_widget import SuggestionItemWidget
from textual.widget import Widget
from textual.widgets import Button
from textual.app import ComposeResult

class PlaylistWidget(SuggestionItemWidget):

	def __init__(self, playlist: Playlist):
		self.playlist = playlist
		super().__init__(playlist.item_type, playlist.title)